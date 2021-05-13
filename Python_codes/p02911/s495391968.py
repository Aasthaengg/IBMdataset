N, K, Q = map(int, input().split())
win_count = [0 for _ in range(N)]
for _ in range(Q):
    win_count[int(input()) - 1] += 1
for i in range(N):
    if K - (Q - win_count[i]) > 0:
        print('Yes')
    else:
        print('No')
