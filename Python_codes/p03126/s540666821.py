N, M = map(int, input().split())
Foods = [0]*(M+1)
for i in range(N):
    K = list(map(int, input().split()))
    for j in range(1, K[0]+1):
        Foods[K[j]] += 1
cnt = 0
for i in range(M+1):
    if Foods[i] == N:
        cnt += 1
print(cnt)