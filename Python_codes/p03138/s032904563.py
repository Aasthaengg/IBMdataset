import bisect
import sys


input = sys.stdin.readline
sys.setrecursionlimit(100000)


class v:
    def __init__(self, f):
        self.f = f
        self.v = None

    def __str__(self):
        return str(self.v)

    def ud(self, n):
        if self.v is None:
            self.v = n
        else:
            self.v = self.f(self.v, n)


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def f(N, M, b_k, D, i):
    res = 0
    for d in range(D - 1, i, -1):
        res += 2 ** d * (M[d] if b_k[d] == "0" else N - M[d])

    res += 2 ** i * M[i]

    for j in range(i):
        res += 2 ** j * (M[j] if M[j] * 2 > N else N - M[j])

    return res


def main():
    N, K = read_values()
    A = read_list()
    T = max(K + 1, max(A))
    D = len(bin(T)) - 2

    M = [0] * D
    for a in A:
        b = format(a, "0" + str(D) + "b")
        for i, s in enumerate(b):
            M[i] += int(s)

    M.reverse()
    b_k = format(K + 1, "0" + str(D) + "b")[::-1]
    res = v(max)
    for i in range(D):
        if b_k[i] == "0":
            continue
        res.ud(f(N, M, b_k, D, i))

    print(res)


if __name__ == "__main__":
    main()
