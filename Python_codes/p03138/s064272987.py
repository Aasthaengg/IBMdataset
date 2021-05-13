N, K = map(int, input().split())
L = K.bit_length()
D = [0]*(L+1)
A = list(map(int, input().split()))
for a in A:
    for i in range(L+1):
        D[i] += (a>>i)&1
res = 0
flg = True
for i in reversed(range(L+1)):
    if flg == False:
        if D[i]<=N//2:
            res += (N-D[i])*pow(2,i)
        else:
            res += D[i]*pow(2, i)
    else:
        if D[i]<=N//2:
            if (K>>i)&1==1:
                res += (N-D[i])*pow(2, i)
            else:
                res += D[i]*pow(2, i)
        else:
            if (K>>i)&1==1:
                flg = False
            res += D[i]*pow(2, i)
mask = 0
for i in range(L+1,43):
    mask += 1<<i
for a in A:
    res += a&mask
print(res)