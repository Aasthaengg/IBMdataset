import itertools
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
seq=[]
for i in range(N):
    seq.append(i+1)
l=list(itertools.permutations(seq))
print(abs(l.index(P)-l.index(Q)))