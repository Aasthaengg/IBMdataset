import collections
N=int(input())
L=list()
for i in range(N):
  L.append(int(input()))
c = collections.Counter(L)
a=list(c.values())
a=[i%2 for i in a]
print(sum(a))