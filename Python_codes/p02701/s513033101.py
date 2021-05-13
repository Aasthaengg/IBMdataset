n=int(input())
s=[]
for i in range(n):
    s.append(input())
a=sorted(s)
ans=1
for q in range(n-1):
    if a[q]!=a[q+1]:
        ans+=1
print(ans)
