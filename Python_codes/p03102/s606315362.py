n, m, c = map(int, input().split())
B = list(map(int, input().split()))

ans = 0
for i in range(n):
    A = list(map(int, input().split()))
    s = c
    for a, b in zip(A, B):  s += a*b
    if s > 0:  ans += 1

print(ans)
