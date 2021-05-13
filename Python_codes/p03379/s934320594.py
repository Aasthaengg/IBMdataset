N=int(input())
L=list(map(int,input().split()))
n=N//2
R=sorted(L)
for i in L:
  if i>R[n-1]:
    print(R[n-1])
  else:
    print(R[n])