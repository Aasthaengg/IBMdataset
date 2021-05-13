def judge(n,array1,array2,K):
    for i in range(n+1):
        if len(array1) > i and len(array2) > n-i:
            sum = array1[i] + array2[n-i]
            if sum <= K:
                return True
    return False

N, M, K = list(map(int,input().split()))
As = list(map(int,input().split()))
Bs = list(map(int,input().split()))

cum_sum_As = [0]
cum_sum_Bs = [0]

sum_As = 0
for i in range(N):
    sum_As += As[i]
    cum_sum_As.append(sum_As)

sum_Bs = 0
for i in range(M):
    sum_Bs += Bs[i]
    cum_sum_Bs.append(sum_Bs)

l = 0
r = N + M
while(r-l>1):
    mid = (l+r)//2
    if judge(mid,cum_sum_As,cum_sum_Bs,K):
        l = mid
    else:
        r = mid

if judge(r,cum_sum_As,cum_sum_Bs,K):
    print(r)
else:
    print(l)
