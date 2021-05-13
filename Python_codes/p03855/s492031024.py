n, k, l = map(int,input().split())
P = [list(map(int,input().split())) for i in range(k)]
R = [list(map(int,input().split())) for i in range(l)]

PM = [[] for i in range(n+1)]
RM = [[] for i in range(n+1)]

for i in range(k):
    PM[P[i][0]].append(P[i][1])
    PM[P[i][1]].append(P[i][0])
for i in range(l):
    RM[R[i][0]].append(R[i][1])
    RM[R[i][1]].append(R[i][0])

C = [[0] * 2 for i in range(n+1)]

VP = [0] * (n+1)
clr = 0
for i in range(1, n+1):
    if VP[i] == 0:
        VP[i] = 1
        clr += 1
        Q = [i]
        st = 0
        while st < len(Q):
            j = Q[st]
            C[j][0] = clr
            for item in PM[j]:
                if VP[item] == 0:
                    VP[item] = 1
                    Q.append(item)
            st += 1

VR = [0] * (n+1)
clr = 0
for i in range(1, n+1):
    if VR[i] == 0:
        VR[i] = 1
        clr += 1
        Q = [i]
        st = 0
        while st < len(Q):
            j = Q[st]
            C[j][1] = clr
            for item in RM[j]:
                if VR[item] == 0:
                    VR[item] = 1
                    Q.append(item)
            st += 1

# print(C)

D = {}
for i in range(1, n+1):
    try:
        D[(C[i][0], C[i][1])] += 1
    except:
        D[(C[i][0], C[i][1])] = 1

ANS = []

for i in range(1, n+1):
    ANS.append(str(D[(C[i][0], C[i][1])]))

print(" ".join(ANS))

