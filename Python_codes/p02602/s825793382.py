N, K = map(int, input().split())
score = list(map(int, input().split()))
for i in range(K, N):
    print("Yes" if score[i - K] < score[i] else "No")
