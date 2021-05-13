N=int(input())
A=[list(map(int,input().split())) for i in range(N)]
B=[]
c=0
for i in range(N):
  a=A[i][0]+A[i][1]
  c-=A[i][1]
  B.append(a)
B=sorted(B)[::-1]
d=(N+1)//2
for i in range(d):
  c+=B[2*i]
print(c)