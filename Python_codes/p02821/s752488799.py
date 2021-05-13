from itertools import groupby,accumulate
import bisect
n,m = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
A.sort()
le=len(A)
#print(A)
B=list(accumulate([0]+A))
ok=0 #可能
ng=10**10 #不可能
ans=0
while 1<abs(ng-ok):
  mid=(ng+ok)//2
  ans=0
  cnt=0
  for i in range(le):
    x = mid-A[i]
    cnt1=int(bisect.bisect_left(A,x))
    cnt+=(le-cnt1)
    #ans+=A[i]*(le-cnt1)+B[n]-B[cnt1]
  if cnt>=m:
    ok=mid
  else:
    ng=mid
cnt=0
for i in range(le):
  x=ok-A[i]
  cnt1=int(bisect.bisect_left(A,x))
  cnt+=le-cnt1
  ans+=A[i]*(le-cnt1)+B[n]-B[cnt1]
print(ans+(m-cnt)*ok)