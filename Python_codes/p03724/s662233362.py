n,m = map(int,input().split())
ans = "YES"
cnt = [0]*n
for _ in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    cnt[a] += 1
    cnt[b] += 1
for i in range(n):
    if cnt[i]%2 != 0:
        ans = "NO"
        break
print(ans)