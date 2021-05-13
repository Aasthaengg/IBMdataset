S=input()
N=len(S)
for i in range((N-1)//2,0,-1):
  A=0
  for j in range(i):
    if S[j]!=S[j+i]:
      A=1
      break
  if A==0:
    print(2*i)
    break