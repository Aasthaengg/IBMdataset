n = int(input())
d = list(map(int, input().split()))

conbination = int((n * (n-1)) / 2)
ans = 0

for i in range(n-1):
    for j in range(i+1,n):
        ans += d[i] * d[j]

print(ans)