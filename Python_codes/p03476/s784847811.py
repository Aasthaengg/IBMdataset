import math
def eraP(n):
    if n<=1: return [False]*(n+1)
    elif n<=2: return [False, False, True]
    L = [False if i%2==0 or i%3==0 else True for i in range(n)]
    L[0] = False; L[1] = False;
    L[2] = True; L[3] = True; L[5]=True
    limit = math.sqrt(n)
    for i in range(3,n,2):
        if i >= limit: return L
        for s in range(i**2,n,i):
            L[s] = False
    return L

q = int(input())
LR = [[0,0] for _ in range(q)]
for i in range(q):
    LR[i] = list(map(int, input().split()))
P = eraP(pow(10,5)+1)[1:]

sumP = [0,0,0]
for i in range(2,pow(10,5)):
    sumP.append(sumP[-1]+int(P[i] and P[(i+1)//2]))

for lr in LR:
    print(sumP[lr[1]]-sumP[lr[0]-1])