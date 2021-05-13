import itertools
l=list(map(int,input().split()))
L=[]
p=itertools.permutations(l,2)
for a,b in p:
  L.append(a+b)
print(min(L))