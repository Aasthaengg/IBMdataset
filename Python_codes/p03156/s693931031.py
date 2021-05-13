N=int(input())
A,B=map(int,input().split())
P=list(map(int,input().split()))
C=[0]*3
for i in range(N):
  if(P[i]<=A):
    C[0]+=1
  elif(P[i]<=B):
    C[1]+=1
  else:
    C[2]+=1
C.sort()
print(C[0])