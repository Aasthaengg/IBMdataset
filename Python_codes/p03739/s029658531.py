n = int(input())
A = list(map(int,input().split()))

ans = float('inf')

cA = A[:]
cs = 0
cnt = 0
for i, a in enumerate(cA):
    if i%2 == 0: #ここまでの累積和が正
        if cs + a > 0:
            cs += a
        else:
            cA[i] += 1-(cs+a)
            cnt += 1-(cs+a)
            cs = 1
    else:
        if cs + a < 0:
            cs += a
        else:
            cA[i] += -1-(cs+a)
            cnt += abs(-1-(cs+a))
            cs = -1
ans = min(ans,cnt)

cA = A[:]
cs = 0
cnt = 0
for i, a in enumerate(cA):
    if i%2 == 1: #ここまでの累積和が正
        if cs + a > 0:
            cs += a
        else:
            cA[i] += 1-(cs+a)
            cnt += 1-(cs+a)
            cs = 1
    else:
        if cs + a < 0:
            cs += a
        else:
            cA[i] += -1-(cs+a)
            cnt += abs(-1-(cs+a))
            cs = -1
ans = min(ans,cnt)
print(ans)