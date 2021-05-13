from itertools import permutations
 
N = int(input())
Nlist = [i for i in range(1, N+1)] 
Nlist = list(permutations(Nlist)) 
 
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
 
print(abs(Nlist.index(P) - Nlist.index(Q)))