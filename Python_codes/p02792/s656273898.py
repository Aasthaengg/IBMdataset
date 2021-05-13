N = int(input())
A=[0]*100
for i in range(1,N+1):
  first=int(str(i)[0])
  last=int(str(i)[-1])
  A[first*10+last]+=1
score=0
for i in range(10):
  for j in range(10):
    score+=A[i*10+j]*A[j*10+i]
print(score)