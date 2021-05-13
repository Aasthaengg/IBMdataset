n = int(input())
p = list(map(int, input().split()))
ans = 0
for i in range(1, n-2+1):
    a = [p[i-1], p[i], p[i+1]]
    a.sort()
    if p[i] == a[1]:
        ans += 1

print(ans)
