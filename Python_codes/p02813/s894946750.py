from itertools import permutations
N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))
for i,p in enumerate(permutations(range(1,N+1))):
    if p == P:
        pi = i
    if p == Q:
        qi = i

print(abs(pi-qi))