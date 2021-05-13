S = input()
N = len(S)

Rcnt = 0
SR = [0]*N
for i in range(N):
    if S[i] == 'R':
        Rcnt += 1
    elif Rcnt== 0:
        continue
    else:
        SR[i] = Rcnt//2
        SR[i-1] = Rcnt - Rcnt//2
        Rcnt = 0
        
SL = [0]*N
SS = S[-1::-1]
Lcnt = 0
for i in range(N):
    if SS[i] == 'L':
        Lcnt += 1
    elif Lcnt ==0:
        continue
    else:
        SL[i] = Lcnt//2
        SL[i-1] = Lcnt - Lcnt//2
        Lcnt = 0

for i in range(N):
    print(SR[i]+SL[N-i-1], end = " ")
