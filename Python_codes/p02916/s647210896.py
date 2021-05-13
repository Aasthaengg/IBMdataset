n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

ans=sum(b)

for i, aa in enumerate(a):
  if i==n-1:
    break
  if a[i]+1==a[i+1]:
    ans+=c[a[i]-1]

print(ans)

