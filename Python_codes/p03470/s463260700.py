N=int(input())
ls=[int(input()) for i in range(N)]
ls=sorted(ls,reverse=True)
A=0
i=0
while i<N-1:
  if ls[i]==ls[i+1]:
    A=A+1
  i=i+1
print(N-A)