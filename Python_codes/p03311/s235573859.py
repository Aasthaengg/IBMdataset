n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
  arr[i]=arr[i]-(i+1)
arr=sorted(arr)
if n%2==1:
  m=arr[n//2]
  ans=0
  for i in range(n):
    ans=ans+abs(arr[i]-m)
  print(ans)
else:
  m1=arr[n//2]
  m2=arr[n//2-1]
  ans1=0
  ans2=0
  for i in range(n):
    ans1=ans1+abs(arr[i]-m1)
    ans2=ans2+abs(arr[i]-m2)
  print(min(ans1,ans2))