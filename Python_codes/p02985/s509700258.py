import collections
def main():

    N, K = map(int, input().split())
    if K == 1:
        if N == 1: return 1
        else: return 0

    tree = collections.defaultdict(list)
    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    mod = pow(10, 9) + 7

    v = inv_factorial(K-1, mod)
    invf = [v]
    for i in range(K-1, 0, -1):
        invf.append((invf[-1] * i) % mod)
    invf = invf[::-1]

    f = [1]
    for i in range(1, K):
        f.append((f[-1]*i) % mod)

    ans = K
    cur = []
    visited = set([1])
    for b in tree[1]:
        cur.append(b)
        visited.add(b)
    l = len(cur)
    if l > K-1: return 0
    ans *= (f[K-1]*invf[K-1-l]) % mod
    ans %= mod

    while cur:
        temp = []
        for a in cur:
            l = len(tree[a])-1
            if l > K-2: return 0
            ans *= (f[K-2]*invf[K-2-l]) % mod
            ans %= mod
            for b in tree[a]:
                if b not in visited:
                    temp.append(b)
                    visited.add(b)
        cur = temp

    return ans


def quickpow(x, y, mod):
    if y == 0: return 1
    elif y == 1: return x
    elif y % 2 == 0: return pow(quickpow(x, y//2, mod), 2) % mod
    elif y % 2 == 1: return (pow(quickpow(x, y//2, mod), 2) * x) % mod

def factorial(x, mod):
    v = 1
    for i in range(2, x+1):
        v *= i
        v %= mod
    return v

def inv_factorial(x, mod):
    v = factorial(x, mod)
    return quickpow(v, mod-2, mod)


if __name__ == '__main__':
    print(main())