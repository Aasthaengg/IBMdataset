from itertools import combinations

inputs = []
n,x = map(int,input().split())
while n != 0 or x != 0:
     inputs.append((n,x))
     n,x = map(int,input().split())

for n,x in inputs:
    print(len([c for c in combinations(range(1,n+1),3) if sum(c) == x]))
