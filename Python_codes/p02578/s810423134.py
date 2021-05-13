N=int(input())
A=list(map(int,input().split()))
B=sum(A)
result=0
for i in range(0,N-1):
  #print(i)
  #print(A[i])
  #print(A[i+1])
  if A[i]>A[i+1]:
    #result=result+(A[i]-A[i+1])
    A[i+1]=A[i]
    #print(result)

print(sum(A)-B)
