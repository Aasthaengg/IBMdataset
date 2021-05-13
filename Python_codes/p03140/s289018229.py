N=int(input())
Sts=[list(input()) for i in range(3)]
ret=0
for i in range(N):
  ret+=len(set([Sts[0][i],Sts[1][i],Sts[2][i]]))-1
print(ret)