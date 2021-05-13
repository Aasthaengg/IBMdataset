import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

H, W = mapint()
S = [list(input()) for _ in range(H)]
ans = [['#']*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        cnt = 0
        for h in range(-1, 2):
            for w in range(-1, 2):
                nh = i + h
                nw = j + w
                if nh<0 or nh>=H or nw<0 or nw>=W:
                    continue
                if S[nh][nw]=='#':
                    cnt += 1
        ans[i][j] = str(cnt)

for a in ans:
    print(''.join(a))