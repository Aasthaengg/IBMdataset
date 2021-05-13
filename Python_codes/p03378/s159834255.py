n,m,x=map(int,input().split())
a=list(map(int, input().split()))
a=sorted(a)
tmp=0
for i in range(m):
    if x<a[i]:
        tmp=i
        break
print(min(tmp,m-tmp))