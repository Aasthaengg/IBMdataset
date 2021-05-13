
n,m,d = map(int,input().split())

k = 2*(n-d)
if d==0:
    k = n
ans = (m-1)*k/(n*n)
print(ans)
