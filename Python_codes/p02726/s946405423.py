from collections import Counter
N, X, Y = map(int, input().split())
cnt = []

for i in range(1, N):
    for j in range(i+1, N+1):
        cnt.append(min(j-i, abs(X-i)+abs(Y-j)+1))

cnt = Counter(cnt)
for i in range(1, N):
    print(cnt[i])

