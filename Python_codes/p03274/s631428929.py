N, K = map(int, input().split())
Xs = list(map(int, input().split()))

global_min = float('inf')
for i in range(N-K+1):
    left = i
    right = i+K-1
    #print(left, right)

    if 0 <= Xs[left]:
        local_min = Xs[right]
    elif Xs[right] <= 0:
        local_min = abs(Xs[left])
    else: # 先にマイナス側に行く場合と、先にプラス場合に行く場合がある。
        tmp1 = 2 * abs(Xs[left]) + Xs[right]
        tmp2 = abs(Xs[left]) + 2 * Xs[right]
        local_min = min(tmp1, tmp2)

    global_min = min(global_min, local_min)

if global_min == float('inf'):
    print(0)
else:
    print(global_min)
