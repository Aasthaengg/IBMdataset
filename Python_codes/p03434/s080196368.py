N=input()
N=int(N)
ls=[int(s) for s in input().split()]
ls=sorted(ls,reverse=True)
A=0
B=0
i=0
while i<N:
  if i%2==0:
    A=A+ls[i]
  if i%2==1:
    B=B+ls[i]
  i=i+1
print(A-B)