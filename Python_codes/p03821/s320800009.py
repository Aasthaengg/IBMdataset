N = int(input())
import math

A = []
B = []
for i in range(N):
  a, b = map(int,input().split())
  A.append(int(a))
  B.append(int(b))

n=0
for i in range(N):
  #print(i,A[N-1-i]+n,B[N-1-i]+n)
  
  if (A[N-1-i]+n)%(B[N-1-i])==0:
    n+=0
  elif A[N-1-i]+n>B[N-1-i]:
    n+=math.ceil((A[N-1-i]+n)/B[N-1-i])*(B[N-1-i])-A[N-1-i]-n
    #print('!',n,math.ceil((A[N-1-i]+n)/(B[N-1-i])))
  elif A[N-1-i]+n<B[N-1-i]:
    n+= B[N-1-i]-A[N-1-i]-n
  #print(n)  
    
  #count +=n
  #print(n)
  #for j in range(N-i):
    #A[j]+=n

print(n)