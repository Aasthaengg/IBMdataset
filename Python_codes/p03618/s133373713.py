s=list(input())
al=list('abcdefghijklmnopqrstuvwxyz')
d=[0]*26
for i in s:
    d[al.index(i)]+=1
n=len(s)
ans=n*(n-1)//2+1
for i in d:
    ans-=i*(i-1)//2
print(ans)