n,k = map(int,input().split())
l = list(map(int,input().split()))
ans = 0
for i in range(k):
    e = max(l)
    ans += e
    l.remove(e)
print(ans)