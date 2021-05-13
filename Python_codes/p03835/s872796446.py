k, s = map(int, input().split())
cnt = 0
for i in range(k+1):
    for j in range(k+1):
        c = s - (i + j)
        if 0 <= c <= k and s == i + j + c:
            cnt += 1

print(cnt)