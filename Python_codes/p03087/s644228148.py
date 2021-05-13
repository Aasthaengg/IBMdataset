n,q = map(int,input().split())
s = list(input())
LR = [0]*q
for i in range(q):
    LR[i] = list(map(int,input().split()))
d = [0]*(n+1)
for i in range(n-1):
    if s[i] == "A" and s[i+1] == "C":
        d[i+1] += d[i] + 1
    else:
        d[i+1] = d[i]
for L,R in LR:
    print(d[R-1]-d[L-1])