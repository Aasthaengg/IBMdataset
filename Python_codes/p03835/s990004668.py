k, s = map(int, input().split())
cnt = 0
for i in range(min(k+1, s+1)):
    for j in range(min(k+1, s-i+1)):
        if s-i-j<=k:
            cnt += 1
print(cnt)
