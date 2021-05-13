N,M=map(int,input().split())
A=[list(map(int,input().split())) for i in range(M)]
B,C=zip(*A)
D=B+C
import collections
a=collections.Counter(D)
for i in a.values():
  if i%2==1:
    print('NO')
    exit()
print('YES')