N = int(input())
T = [0]*5
for i in range(N):
    S = input()
    if S[0]=="M":
        T[0]+=1
    elif S[0]=="A":
        T[1]+=1
    elif S[0]=="R":
        T[2]+=1
    elif S[0]=="C":
        T[3]+=1
    elif S[0]=="H":
        T[4]+=1
from itertools import combinations
Ls = list(combinations([0,1,2,3,4],3))
out = 0
for L in Ls:
    out += T[L[0]]*T[L[1]]*T[L[2]]
print(out)