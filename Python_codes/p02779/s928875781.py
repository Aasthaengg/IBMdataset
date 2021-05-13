import collections
N=int(input())
A=list(map(int,input().split()))
li=list(collections.Counter(A).values())
for i in range(len(li)):
  if li[i]>1:
    print('NO')
    exit()
print('YES')