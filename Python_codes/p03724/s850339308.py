n,m = map(int,input().split())
c = [0]*n
for i in range(m):
    a,b = map(lambda x: int(x)-1,input().split())
    c[a]+=1
    c[b]+=1
ans = 'YES'
for i in c:
    if i%2==1:
        ans = 'NO'
print(ans)