import sys
input = sys.stdin.buffer.readline


h, w, n = map(int,input().split())
d = {}
for i in range(n):
    ch, cw = map(int,input().split())
    for dh in [-1,0,1]:
        for dw in [-1,0,1]:
            if 2 <= ch + dh <= h-1 and 2 <= cw + dw <= w-1:
                x = (ch + dh)*10**10 + cw + dw
                # print(ch, cw, dh, dw, x)
                if x in d:
                    d[x] += 1
                else:
                    d[x] = 1
ans = [0] * 10
ans[0]
for v in d.values():
    ans[v] += 1
ans[0] = (h-2)*(w-2) - sum(ans[1:])
for i in range(10):
    print(ans[i])
