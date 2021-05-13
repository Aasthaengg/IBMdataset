
N, K, Q = map(int, input().split())
X = [int(input()) for _ in range(Q)]

cnt = [0] * N
for q in X:
    cnt[q - 1] += 1

for i in range(N):
    if Q - cnt[i] >= K:
        print("No")
    else:
        print("Yes")
