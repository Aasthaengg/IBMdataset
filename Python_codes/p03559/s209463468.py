n=int(input())
A=sorted([int(i) for i in input().split()])
B=sorted([int(i) for i in input().split()])
C=sorted([int(i) for i in input().split()])
import bisect
ans=0
for i in range(n):
  b=B[i]
  ans+=bisect.bisect_left(A,b)*(n-bisect.bisect_right(C,b))
print(ans)