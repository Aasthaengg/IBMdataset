n = int(input())

A, B = 0, 10**9+1

for _ in range(n):
    a, b = map(int, input().split())
    A = max(A, a)
    B = min(B, b)

print(A+B)