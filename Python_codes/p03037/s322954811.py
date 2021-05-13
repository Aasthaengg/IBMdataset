n,m = map(int,input().split())


l = [1]*n
L,R = 0,float('inf')
for _ in range(m):
    a,b = map(int,input().split())
    L = max(L,a)
    R = min(R,b)
ans = R-L+1
if ans<=0:ans = 0
print(ans)
