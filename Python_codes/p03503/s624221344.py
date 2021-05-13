N = int(input())
F = [[int(i) for i in input().split()] for j in range(N)]
P = [[int(i) for i in input().split()] for j in range(N)]

ci = 0
c = []
P_max = -1000000000
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                for m in range(2):
                    for n in range(2):
                        for o in range(2):
                            for p in range(2):
                                for q in range(2):
                                    for r in range(2):
                                        if i==0 and j==0 and k==0 and l==0 and m==0 and n==0 and o==0 and p==0 and q==0:
                                            r = 1
                                        P_sample = 0
                                        for s in range(N):
                                            ci = F[s][0]*i + F[s][1]*j + F[s][2]*k + F[s][3]*l + F[s][4]*m + F[s][5]*n + F[s][6]*o + F[s][7]*p + F[s][8]*q + F[s][9]*r
                                            P_sample += P[s][ci]
                                        P_max = max(P_max, P_sample)

print(P_max)
