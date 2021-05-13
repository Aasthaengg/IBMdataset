import math

N,D=(int(x) for x in input().split())

answer=0
for i in range(N):
  A,B=(int(x) for x in input().split())
  h=math.sqrt(A*A+B*B)
  if  D>=h:
    answer+=1
print(answer)
