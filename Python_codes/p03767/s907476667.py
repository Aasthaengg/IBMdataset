n=int(input())
a=[0]*(3*n)
a=list(map(int,input().split()))
a=sorted(a,reverse=True)
ans=0
#print(a)
for i in range(n):
  ans+=a[2*i+1]
print(ans)