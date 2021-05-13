N, K, C = map(int, input().split())
S = input().strip()
dp1 = [0]*(N+2)
dp2 = [0]*(N+2)
c = 10*18
cc = 0
for i in range(N):
    if S[i] == "o" and c >= C:
        cc += 1
        c = 0
    else:
        c += 1
    dp1[i+1] = cc
c = 10*18
cc = 0
for i in range(N-1, -1, -1):
    if S[i] == "o" and c >= C:
        cc += 1
        c = 0
    else:
        c += 1
    dp2[i+1] = cc
rs = []
for i in range(N):
    if S[i] == "o" and dp1[i] + dp2[i+2] == K-1 and dp1[i+1] + dp2[i+1] - 1 == K:
        rs.append(i+1)

#print(dp1, dp2)
for r in rs:
    print(r)
