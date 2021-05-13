import itertools
N = int(input())
A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))
p = itertools.permutations(range(1,N+1),N)
hashmap = {}
for i, v in enumerate(p):
    hashmap[v]=i+1
print(abs(hashmap[A]-hashmap[B]))