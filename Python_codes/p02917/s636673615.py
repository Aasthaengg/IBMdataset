N=int(input())
B=list(map(int,input().split()))

if N==2:print(B[0]*2)
else:
  A = [B[0]]
  for i in range(N-2):
    A.append(min(B[i],B[i+1]))
  A.append(B[-1])
  print(sum(A))