n=int(input())
a=sorted(list(map(int,input().split())))
ai=a[-1]
aa=ai/2
ans=float("inf")
for i in range(n-1):
    tmp=abs(a[i]-aa)
    if tmp<ans:
        ans=tmp
        aj=a[i]
print(ai,aj)