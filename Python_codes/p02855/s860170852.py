import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

H, W, K = mapint()
cake = [list(str(input())) for _ in range(H)]
ans = [['0']*W for _ in range(H)]
cnt = 0
unchecked_row = [0]*H
for h in range(H):
    row = cake[h]
    if '#' in row:
        cnt += 1
        first = 1
        for i, r in enumerate(row):
            if r=='.':
                ans[h][i] = str(cnt)
            else:
                if first:
                    first=0
                    ans[h][i] = str(cnt)
                    continue
                cnt += 1
                ans[h][i] = str(cnt)
    else:
        unchecked_row[h] = 1
for i, unchecked in enumerate(unchecked_row):
    if unchecked:
        for j in range(1, H):
            if i-j>=0 and not unchecked_row[i-j]:
                ans[i] = ans[i-j][:]
                unchecked_row[i] = 0
                break
            elif i+j<=H and not unchecked_row[i+j]:
                ans[i] = ans[i+j][:]
                unchecked_row[i] = 0
                break
for h in range(H):
    print(' '.join(ans[h]))