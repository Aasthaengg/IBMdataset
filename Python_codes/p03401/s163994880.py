from sys import stdin
inp = stdin.readline

N = int(inp())
A = list(map(int, inp().split()))

A.insert(0, 0)
A.append(0)


def money(a, b):
    return (abs(a - b))


sumall = 0

for i in range(len(A) - 1):
    sumall += money(A[i], A[i + 1])

for i in range(1, len(A) - 1):
    ans = sumall
    ans -= (money(A[i - 1], A[i]) + money(A[i], A[i + 1]))
    ans += money(A[i - 1], A[i + 1])
    print(ans)
