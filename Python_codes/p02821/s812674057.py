import bisect
N, M = list(map(int,input().split()))
data = list(map(int,input().split()))
data.sort()
def cost(x):
    re = 0
    for i in range(N):
        idx = bisect.bisect_left(data,x - data[i])
        re += N - idx
    return re
#binery_search
lb = 0
ub = 2*max(data) + 1
while ub - lb > 1:
    mid = (ub+lb)//2
    if cost(mid) >= M:
        lb = mid
    else:
        ub = mid
ans = 0 - (cost(lb) - M)* lb
cum_data = [0]*(N+1)
for i in range(1,N+1):
    cum_data[i] = cum_data[i -1] + data[i-1]
data_idx = [0]*N
for i in range(N):
    idx = bisect.bisect_left(data,lb - data[i])
    data_idx[i] = idx
for i in range(N):
    ans += (N - data_idx[i]) * data[i]
    ans += cum_data[N] - cum_data[data_idx[i]]
print(ans)