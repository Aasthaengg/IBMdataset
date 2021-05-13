N=int(input())
A=[]
B=[]
x=[]
c=0
for i in range(N):
    y=list(map(int,input().split()))
    A.append(y[0])
    B.append(y[1])
for i in range(N-1,-1,-1):
  x=A[i]
  y=B[i]
  if (x+c)%y!=0:
    c+=y-(x+c)%y
print(c)