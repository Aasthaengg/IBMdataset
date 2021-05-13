n,h,w = map(int,input().split())
a=[]
b=[]
for _ in range(n):
    aa,bb = map(int,input().split())
    a.append(aa)
    b.append(bb)
ans = 0
for i in range(n):
    ans += min(a[i]//h,b[i]//w)**2
print(ans)