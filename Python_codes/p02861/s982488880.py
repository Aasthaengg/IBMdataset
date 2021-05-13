import math
import itertools
n=int(input())
L=[list(map(int,input().split())) for _ in range(n)]

perm= math.factorial(n)
s = 0

M=[]
for v in itertools.permutations(L, n):
    M.append(list(v))


for i in range(perm):
    for j in range(n-1):
        s += math.sqrt((M[i][j][0] - M[i][j+1][0])**2 +(M[i][j][1] - M[i][j+1][1])**2)
print(s/perm)
