n=str(input())
N=list(n)
t=0
for i in range(len(N)):
  if N[i]=='2':
    t+=1
print(t)