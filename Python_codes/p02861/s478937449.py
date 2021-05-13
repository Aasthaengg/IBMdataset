from math import *
N=int(input())
L=[list(map(int,input().split())) for i in range(N)]
S=0
for i in range(N):
    for j in range(N):
        S+=sqrt((L[i][0]-L[j][0])**2+(L[i][1]-L[j][1])**2)
print(S/N)