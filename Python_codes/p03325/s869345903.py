import math
N=int(input())
a=list(map(int,input().split()))
ans=0
for i in a:
  ans+=math.log2(i & -i)
print(int(ans))