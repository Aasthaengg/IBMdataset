a,b,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = min(a) + min(b)

for i in range(m):
    x,y,c = list(map(int,input().split()))
    res = a[x-1] + b[y-1] - c
    ans = min(ans,res)
    
print(ans)