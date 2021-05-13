N=int(input())
A=list(map(int,input().split()))
L=[0]*N
for a in A:
  L[a-1]+=1
print(*L,sep='\n')