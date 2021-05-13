n=int(input())
a=list(map(int,input().split()))
ans=0
counter=0
for i in range(1,n):
  if a[i]>a[i-1]:
    counter=0
  else:
    counter+=1
    ans=max(ans,counter)
print(ans)
