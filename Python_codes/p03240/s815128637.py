import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
xyh = [None]*n
for i in range(n):
    x,y,h = map(int, input().split())
    xyh[i] = (x,y,h)
ans = []
bx,by,bh = max(xyh, key=lambda p: p[2])
for i in range(101):
    for j in range(101):
        H = bh + abs(bx-i) + abs(by-j)
        bad = False
        for x,y,h in xyh:
            if max(0, H - abs(x-i) - abs(y-j))!=h:
                bad = True
                break
        if bad:
            pass
        else:
            ans = (i,j,H)
            break
    if not bad:
        break
print(" ".join(map(str, ans)))