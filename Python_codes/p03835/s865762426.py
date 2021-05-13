K, S = map(int, input().split())
ans = 0
for i in range(0,K+1):
    for j in range (0,K+1):
        if (S-K) <= (i + j) <= S:
            ans += 1
            continue
print(ans)