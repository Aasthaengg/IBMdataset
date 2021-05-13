import collections

N=int(input())
D=collections.Counter(list(map(int,input().split())))
M=int(input())
T=list(map(int,input().split()))

for i in range(M):
  temp=T[i]
  D[temp]-=1
  if D[temp]==-1:
    print('NO')
    break
else:
  print('YES')