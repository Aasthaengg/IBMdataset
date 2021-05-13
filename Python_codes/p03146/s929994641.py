# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

S = int(input())


def f(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


List_A = [S]
for i in range(10 ** 6):
    A = f(List_A[i])
    if A in List_A:
        print(i+1+1)
        break
    else:
        List_A.append(A)
