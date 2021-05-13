import itertools

n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))

lis=sorted(p)

for i,j in enumerate(itertools.permutations(lis)):
  if list(j)==p:
    a=i
  if list(j)==q:
    b=i
    
print(abs(a-b))