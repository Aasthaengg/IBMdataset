n = int(input())
F = [[*map(int, input().split())] for _ in range(n)]
P = [[*map(int, input().split())] for _ in range(n)]

def c(i, open_pattern):
    ret = 0
    for j in range(10):
        if open_pattern>>j & 1: #open my shop
            if F[i][j]: ret += 1 # open your shop
    return ret

ans = -10000000*100
for i in range(1, 1<<10): # open pattern 10bit, i:[0~1,1~1]
    s = 0
    for j in range(n): # your shop
        cj = c(j, i)
        s += P[j][cj]
    ans = max(ans ,s)
print(ans)
