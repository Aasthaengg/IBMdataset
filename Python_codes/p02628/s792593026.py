N=list(map(int,input().split()))
S=list(map(int,input().split()))
S.sort()
x=0
for i in range(N[1]):
  x=x+S[i]
print(x)