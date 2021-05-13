n=int(input())
a=list(map(int,input().split()))
s=sum(a)
l=[s]
for i in range(n-1):
 l.append(l[i]-2*a[i])
ans=float("inf")
del l[0]
for i in l:
 ans=min(ans,abs(i))
print(ans)