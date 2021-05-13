n,t=map(int,input().split())
l=list(map(int,input().split()))
#最大利益を実現する買い方の組がいくつあるか考えたい
#ある地点で売るときはそれより前の地点の一番安いところで買うのが良いーnowminで判断しよう
count=0
max=0
nowmin=l[0]
nowmincount=1
for i in range(1,n):
  if l[i]-nowmin>max:
    max=l[i]-nowmin
    count=nowmincount
  elif l[i]-nowmin==max:
    count+=nowmincount
  elif nowmin>l[i]:
    nowmincount=1
    nowmin=l[i]
  elif nowmin==l[i]:
    nowmincount+=1
print(count)