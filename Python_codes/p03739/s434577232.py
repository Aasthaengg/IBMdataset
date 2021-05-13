n=int(input())
a=list(map(int,input().split()))

#正/負いずれかから始める
cost1=0
cost2=0
sum1=0
sum2=0
for i in range(n):
  sum1=sum1+a[i]
  sum2=sum2+a[i]
  if i%2==0:
    if sum1<1:
      cost1+=1-sum1
      sum1=1
    
    if sum2>-1:
      cost2+=1+sum2
      sum2=-1
  else:
    if sum1>-1:
      cost1+=1+sum1
      sum1=-1
    
    if sum2<1:
      cost2+=1-sum2
      sum2=1
print(min(cost1,cost2))