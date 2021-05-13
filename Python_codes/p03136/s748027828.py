n=int(input())
l=list(map(int,input().split()))
allsum=sum(l)
mx = max(l)
if mx < allsum-mx:
  print('Yes')
else:
  print('No')