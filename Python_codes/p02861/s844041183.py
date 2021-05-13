from itertools import permutations
from math import sqrt,factorial
N=int(input())
L=[]
for i in range(N):
    L.append(list(map(int, input().split())))
# print(L)

sum=0
for S in permutations(range(N)):
    tmp=0
    for i in range(N-1):
        tmp+= sqrt((L[S[i]][0]-L[S[i+1]][0])**2 + (L[S[i]][1]-L[S[i+1]][1])**2)
    sum+=tmp
print(sum/factorial(N))