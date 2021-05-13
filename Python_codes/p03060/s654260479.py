n = int(input())
v=list(map(int,input().split()))
c=list(map(int,input().split()))
ans=0
for i in range(0, n):
    a = max(v[i] - c[i], 0)
    ans += a
print(ans)