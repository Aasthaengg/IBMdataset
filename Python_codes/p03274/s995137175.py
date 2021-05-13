import bisect

N,K = (int(x) for x in input().split())
x = list(map(int, input().split()))
bs = bisect.bisect_left(x,0)
ans = float('inf')
if bs == N:
    print(x[-K]*(-1))
    exit()
else:
    if x[bs] == 0:
        x.pop(bs)
        K -= 1
neg = bs
pos = N - bs
if len(x) == 0 or K == 0:
    print('0')
elif neg == 0:
    print(x[K-1])
else:
    for i in range(min(neg,K)+1):
        if i + pos < K:
                continue
        else:
            if i == 0:
                ans = min(ans,x[bs+K-1])
            elif i == K:
                ans = min(ans,x[bs-K]*(-1))
            else:
                tempn = x[bs-i] * (-1)
                tempp = x[bs+K-i-1]
                ans = min(ans,min(tempn,tempp)*2+max(tempn,tempp))
    print(ans)