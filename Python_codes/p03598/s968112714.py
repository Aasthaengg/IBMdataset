n = int(input())
k = int(input())
x = list(map(int, input().split()))

ans = 0

for a in range(n):
    if k - x[a] < x[a]:
        ans += (k - x[a])*2
    else:
        ans += x[a] * 2

print(ans)
