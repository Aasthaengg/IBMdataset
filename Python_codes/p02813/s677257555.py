import itertools
n=int(input())
P=tuple((map(int,input().split())))
Q=tuple((map(int,input().split())))
L=[]

for i in range(n):
    L.append(i+1)
    
M=list(itertools.permutations(L))


print(abs(M.index(P)-M.index(Q)))
