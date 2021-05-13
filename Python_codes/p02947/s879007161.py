import collections
N=int(input())
j=0
L=list()
R=list()
for i in range(N):
  S="".join(sorted(list(input())))
  L.append(S)
c = collections.Counter(L)
counts=c.values()
counts=list(counts)
A=[i*(i-1)//2 for i in counts]
print(sum(A))