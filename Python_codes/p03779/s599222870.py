x=int(input())
sum,cnt=0,0
while sum<=10**9:
  cnt+=1
  if sum<x<=sum+cnt:
    print(cnt)
    break
  sum+=cnt