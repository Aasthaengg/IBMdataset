S=list(input())
N=len(S)

g=0
p=0
for i in range(N):
  if S[i]=="g":
    g+=1
  else:
    p+=1
    
print(g-(N+1)//2)