# E - Dividing Chocolate
import sys
sys.setrecursionlimit(10000)

H,W,K = map(int,input().split())
S = [input() for _ in range(H)]
ans = 10000

def check(border, num):
    global H,W,K,S
    now = [0]*(num+1)
    add = 0
    for j in range(W):
        tmp = [0]*(num+1)
        for i in range(H):
            now[border[i]] += int(S[i][j])
            tmp[border[i]] += int(S[i][j])
        if max(now)>K:
            add += 1
            now = tmp
        if max(tmp)>K:
            return 10000
    return num+add

def rec(border, num, i):
    global H,W,K,S,ans
    if i<H:
        border[i] = num
        rec(border, num, i+1)
        border[i] = num+1
        rec(border, num+1, i+1)
    else:
        ans = min(ans, check(border, num))

rec([0]*H, 0, 1)
print(ans)