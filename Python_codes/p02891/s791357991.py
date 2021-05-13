S = list(input())
K = int(input())
N = len(S)

C0 = []
cnt = 1
for i in range(1,N):
    if S[i]==S[i-1]:
        cnt+=1
        if i==N-1:
            C0.append(cnt)
    else:
        C0.append(cnt)
        cnt = 1
out0 = 0
for m in C0:
    out0 += m//2

if S[0]!=S[-1]:
    out = out0*K
elif N==1:
    out = K//2
elif len(C0)==1:
    X = C0[0]*K
    out = X//2
else:
    X = (C0[0] + C0[-1])//2
    Y = C0[0]//2 + C0[-1]//2
    out = (out0-Y)*K
    out += X*(K-1)
    out += Y
print(out)