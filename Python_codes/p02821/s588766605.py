import sys
INF = 1 << 60
MOD = 10**10 + 1
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()

class NTT(object):
    def __init__(self, prime, root):
        self._prime = prime
        self._root = root

    def _fmt(self, A, inverse = False):
        N = len(A)
        logN = (N - 1).bit_length()
        prime = self._prime
        base = pow(self._root, (prime - 1) // N * (1 - 2 * inverse) % (prime - 1), prime)
        step = N
        for k in range(logN):
            step >>= 1
            w = pow(base, step, prime)
            wj = 1
            nA = [0] * N
            for j in range(1 << k):
                for i in range(1 << logN - k - 1):
                    s, t = i + j * step, i + j * step + (N >> 1)
                    ps, pt = i + j * step * 2, i + j * step * 2 + step
                    nA[s], nA[t] = (A[ps] + A[pt] * wj) % prime, (A[ps] - A[pt] * wj) % prime
                wj = (wj * w) % prime
            A = nA
        return A

    def convolution(self, f, g):
        N = 1 << (len(f) + len(g) - 2).bit_length()
        prime = self._prime
        Ff, Fg = self._fmt(f + [0] * (N - len(f))), self._fmt(g + [0] * (N - len(g)))
        N_inv = pow(N, prime - 2, prime)
        fg = self._fmt([a * b % prime * N_inv % prime for a, b in zip(Ff, Fg)], inverse = True)
        del fg[len(f) + len(g) - 1:]
        return fg

def Garner(R, M):
    n = len(R)
    M.append(MOD)
    coeffs, consts = [1] * (n + 1), [0] * (n + 1)
    for i in range(n):
        a, b, u, v = coeffs[i], M[i], 1, 0
        while b:
            u, v = v, u - a // b * v
            a, b = b, a - a // b * b
        t = (R[i] - consts[i]) * (u % M[i]) % M[i]
        for j in range(i + 1, n + 1):
            consts[j] = (consts[j] + t * coeffs[j]) % M[j]
            coeffs[j] = coeffs[j] * M[i] % M[j]
    M.pop()
    return consts[-1]

class arbitrary_mod_NTT(object):
    def __init__(self, primes, roots):
        self._ntts = [NTT(prime, root) for prime, root in zip(primes, roots)]
        self._primes = primes

    def convolution(self, f, g):
        res = [0] * (len(f) + len(g) - 1)
        fgs = [ntt.convolution(f, g) for ntt in self._ntts]
        for i in range(len(res)):
            res[i] = Garner([fg[i] for fg in fgs], self._primes)
        return res

def resolve():
    n, m = map(int, input().split())
    f = [0] * (100001)
    for a in map(int, input().split()):
        f[a] += 1
    ff = arbitrary_mod_NTT([167772161, 469762049, 1224736769], [3, 3, 3]).convolution(f, f)

    ans = 0
    n = len(ff)
    for i in range(n - 1, -1, -1):
        add = min(m, ff[i])
        m -= add
        ans += i * add

    print(ans)
resolve()