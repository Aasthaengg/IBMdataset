N,K = map(int,input().split())
W = []
for _ in range(N):
    W.append(int(input()))


def is_OK(P):
    track_index = 0
    w_index = 0
    while w_index < N and track_index < K:
        tmp_sum = 0
        while  w_index < N and tmp_sum+W[w_index] <= P:
            tmp_sum += W[w_index]
            w_index += 1
        track_index += 1
    return w_index == N

L = 0
R = 100000*100000
#mid = (L+R)//2
ans = R

while L <= R:
    mid = (L+R)//2
    if is_OK(mid):
        ans = mid
        R = mid-1
    else:
        L = mid+1
    #mid = (L+R)//2

print("%d"%ans)

