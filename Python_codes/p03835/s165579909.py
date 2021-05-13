K, S = map(int, input().split())

cnt = 0
for i in range(K+1):
    for j in range(K+1):
        ij = i + j
        if ij > S:
            break
        if (S - ij <= K):
            cnt += 1
print(cnt)            