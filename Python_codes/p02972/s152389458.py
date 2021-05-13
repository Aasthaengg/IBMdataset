import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = [0] + list(map(int, input().split()))
    B = [0] * (n + 1)
    res = []

    for i in reversed(range(1, n + 1)):
        if B[i] % 2 != A[i]:
            res.append(i)
            for j in range(1, int(pow(i, 0.5)) + 1):
                if i % j == 0:
                    B[j] += 1
                    if j != i // j:
                        B[i // j] += 1

    print(len(res))
    if len(res) != 0:
        print(*res[::-1])


if __name__ == '__main__':
    resolve()
