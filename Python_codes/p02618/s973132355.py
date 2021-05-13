D = int(input())
C = list(map(int,input().split()))
 
s = [[] for _ in range(D)]
last_con = [0]*26
 
def evaluation(x,y,z,a):
    P = [0]*26
    for m in range(26):
        P[m] += x[m]
        for n in range(26):
            if m == n:continue
            P[m] -= a[n]*(z+1-y[n])
    return P.index(max(P))
 
for i in range(D):
    s[i] = list(map(int,input().split()))
 
for i in range(D):
    op = evaluation(s[i],last_con,i,C)
    last_con[op] = i+1
    print(op+1)