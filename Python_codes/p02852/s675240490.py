INFTY = 10**6
N,M = map(int,input().split())
S = input().strip()
S0 = []
for i in range(N+1):
    if S[i]=="0":
        S0.append(i)
flag = 0
for i in range(1,len(S0)):
    if S0[i]-S0[i-1]>M:
        flag = 1
        break
if flag==1:
    print(-1)
else:
    C = [[INFTY,-1,-1] for _ in range(N+1)]
    C[N] = [0,0,N]
    cur = N
    curN = -1
    a = 0
    for i in range(len(S0)-2,-1,-1):
        j = S0[i]
        if cur-j<=M:
            pass
        else:
            cur = curN
            a += 1
        C[j] = [a+1,cur-j,cur]
        curN = j
    i = 0
    A = []
    while i<N:
        A.append(C[i][1])
        i = C[i][2]
    print(*A)