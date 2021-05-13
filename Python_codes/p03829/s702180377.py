N, A, B = map(int, input().split())
x = list(map(int, input().split()))

ans = 0
for i, j in zip(x[:-1], x[1:]):
    c = min(A*(j-i), B)
    ans += c

print(ans)