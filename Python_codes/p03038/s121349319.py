N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
CB=[]
for i in range(M):
  B,C=map(int,input().split())
  CB.append([C,B])
CB.sort(reverse=True)

idx=0
for C,B in CB:
  for i in range(B):
    if not idx>=len(A) and A[idx]<C:
      A[idx]=C
      idx+=1
    else:
      break
print(sum(A))
