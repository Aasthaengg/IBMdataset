n=int(input())
lst=list(map(int,input().split()))
ans=0
temp=0
for i in range(1, n):
  if lst[i]<=lst[i-1]:
    temp+=1
  else:
    if temp>ans:
      ans=temp
    temp=0
if temp>ans:
  ans=temp
print(ans)