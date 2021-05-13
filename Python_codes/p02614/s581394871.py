H, W, K = map(int, input().split())
c = [input() for x in range(H)]
cnt = 0

for i in range(2 ** H - 1):
    for j in range(2 ** W - 1):
        sum = 0
        for ih in range(H):
            if 2 ** ih & i > 0:
                continue
            for iw in range(W):
                if 2 ** iw & j > 0:
                    continue
                if c[ih][iw] == '#':
                    sum += 1
        if sum == K:
            cnt += 1

print(cnt)
