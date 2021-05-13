import itertools
n=int(input())
p=tuple([int(x) for x in input().rstrip().split()])
q=tuple([int(x) for x in input().rstrip().split()])

m=[i+1 for i in range(n)]
l=[i for i in itertools.permutations(m,n)]

now=0
for i in l:
  if i==p:
    a=now
  if i==q:
    b=now
  now+=1
print(abs(a-b))