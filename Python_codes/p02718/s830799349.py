import sys

N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort(reverse=True)
rank=A[:M]
for i in range(M):
  if(rank[i]<sum(A)/(4*M)):
    print("No")
    sys.exit()
print("Yes")
