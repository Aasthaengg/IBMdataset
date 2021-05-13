n = int(input())
p = list(map(int, input().split()))

ans = 0
for i in range(1, n-1):
    a, b, c = p[i-1:i+2]
    if min(a, b, c) < b < max(a, b, c):
        ans += 1

print(ans)
