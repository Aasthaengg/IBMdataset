r,n = map(int,input().split())
ans = []
ans.append(n)
for l in range(r-1):
    ans.append(n + (l + 1))
    ans.append(n - (l + 1))
ans.sort()
print(*ans)
