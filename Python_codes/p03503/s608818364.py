n = int(input())
F = [[*map(int, input().split())] for _ in range(n)]
P = [[*map(int, input().split())] for _ in range(n)]
ans = -10000000*100
for i in range(1, 1<<10): # my shop open pattern 10bit, i:[0~1,1~1]
    s = 0
    for j in range(n): # the other shop
        cj = 0
        for k in range(10):
            if i>>k & 1 and F[j][k]: cj += 1
        s += P[j][cj]
    ans = max(ans ,s)
print(ans)
