R, G, B, n = map(int, input().split())
cnt = 0
for r in range(n+1):
    for g in range(n+1):
        bb = n - r*R - g*G
        if bb < 0:
            break
        elif bb%B == 0:
            cnt += 1
print(cnt)