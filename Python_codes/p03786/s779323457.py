N=int(input())
A=list(map(int,input().split()))
B=sorted(A)
import numpy
C=numpy.cumsum(B)
cnt=1
for i in range(N-1):
  if C[-2-i]*2>=B[-1-i]:
    cnt+=1
  else:
    print(cnt)
    exit()
print(cnt)