N=int(input())
M=list(map(int,input().split()))
M=sorted(M)
C=(M[0]+M[1])/2
for i in range(2,N):
  C=(C+M[i])/2
print(C)