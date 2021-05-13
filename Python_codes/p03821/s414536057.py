# https://atcoder.jp/contests/agc009/tasks/agc009_a

n = int(input())

A = []
B = []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = 0
plus = 0
for i in range(n)[::-1]:
    a = A[i] + plus
    b = B[i]
    if a % b != 0:
        multi = a // b + 1
        t = b * multi - a
        ans += t
        plus += t
print(ans)