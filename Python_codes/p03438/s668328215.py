n=int(input())
*a,=map(int,input().split())
*b,=map(int,input().split())
ans=0
for i in range(n):
  if a[i]>b[i]:
    ans-=a[i]-b[i]
  else:
    ans+=(b[i]-a[i])//2
print('No' if ans<0 else 'Yes')