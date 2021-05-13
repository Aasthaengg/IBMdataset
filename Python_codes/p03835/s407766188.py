K, S = map(int, input().split())
cnt = 0
for i in range(min(K, S) + 1):
    for j in range(min(K, S - i) + 1):
        if i + j >= S - K:
            cnt += 1
print(cnt)