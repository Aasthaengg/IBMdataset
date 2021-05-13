
D = int(input())
C = list(map(int,input().split()))
 
s = [[] for _ in range(D)]
last = [0]*26
 
for i in range(D):
    s[i] = list(map(int,input().split()))

def evaluation(d):
    P = [0]*26
    for i in range(26):
        P[i] += s[d][i]
        for j in range(26):
            if i == j:
                continue
            P[i] -= C[j] * (d+1 - last[j])
    return P.index(max(P))
 
 
for d in range(D):
    d_maxP = evaluation(d)
    last[d_maxP] = d+1
    print(d_maxP + 1)
