import sys
input = sys.stdin.readline

N=int(input())
A=[0]*N
B=[0]*N
C=[0]*N

for i in range(N):
  A[i],B[i] = map(int,input().split())
  C[i]=(A[i],B[i],A[i]+B[i])

t=0
a=0

C.sort(key= lambda x: x[2],reverse=True)
#print(C)
#C.sort(key= lambda x: x[0],reverse=True)
for i in range(N):
  if i%2==0:
    t += C[i][0]
  else:
    a += C[i][1]

print(t-a)