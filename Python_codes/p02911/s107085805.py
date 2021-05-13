N, K, Q = map(int, input().split())
cnt = [0] * N
for _ in range(Q):
    a = int(input())
    cnt[a-1] += 1
for c in cnt:
    if Q - c < K:
        print('Yes')
    else:
        print('No')