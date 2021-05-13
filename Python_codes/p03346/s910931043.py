N = int(input())
P, Q = [], [0]*(N+1)
for i in range(1,N+1):
    p = int(input())
    P.append(p)
    Q[p] = i
Q.append(0)
cnt = 1
res = []
for i in range(1,N+1):
    if Q[i] < Q[i+1]:
        cnt += 1
    else:
        res.append(cnt)
        cnt = 1
if res:
    print(N-max(res))
else:
    print(N)