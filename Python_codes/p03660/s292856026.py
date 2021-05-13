# import sys
# input = sys.stdin.readline

n = int(input())
C = [list(map(int,input().split())) for i in range(n-1)]

V = [0] * (n+1)
P = [-1] * (n+1)

M = [[] for i in range(n+1)]
for i in range(n-1):
    M[C[i][0]].append(C[i][1])
    M[C[i][1]].append(C[i][0])

Q = [1]
s = 0
V[1] = 1
while s < len(Q):
    i = Q[s]
    for x in M[i]:
        if V[x] == 0:
            V[x] = 1
            P[x] = i
            Q.append(x)
    s += 1
    # print(Q)

# print(P)

aida = [n]
a = n
while a != 1:
    a = P[a]
    aida.append(a)



V = [0] * (n+1)
for i in aida:
    V[i] = 1

aida = aida[::-1]
# print(aida)

fe = 0
su = 0
for j in range(len(aida)):
    ans = 1
    Q = [aida[j]]
    s = 0
    while s < len(Q):
        i = Q[s]
        for x in M[i]:
            if V[x] == 0:
                V[x] = 1
                P[x] = i
                Q.append(x)
                ans += 1
        s += 1
    if j < (len(aida)+1)//2:
        fe += ans
    else:
        su += ans
    # print(aida[j],ans)

# print(fe,su)
if fe > su:
    print("Fennec")
else:
    print("Snuke")