D = int(input())
C = list(map(int,input().split()))
 
s = [[] for _ in range(D)]
last = [0]*26
 
for i in range(D):
    s[i] = list(map(int,input().split()))

t = [0]*D
v_day = [0]*D

for d in range(D):
    P = [0]*26
    for i in range(26):
        P[i] += s[d][i]
        for j in range(26):
            if i == j:
                continue
            P[i] -= C[j] * (d+1 - last[j])
    d_maxP = P.index(max(P))
    print(d_maxP + 1)
    last[d_maxP] = d+1
    t[d] = d_maxP + 1
    v_day[d] = s[d][t[d] - 1] - sum([C[k]*(d+1 - last[k]) for k in range(26)])