n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]

ans = -float("inf")
for i in range(1,1 << 10):
    l = [0]*n
    for j in range(10):
        #bin(i)をj桁シフトして0001と&をとる　＝　j桁目が1なら採用
        if ((i >> j) & 1) == 1:
            # fが一日どうか
            for k in range(n):
                if f[k][j] == 1:
                    l[k]+= 1
    
    ansi = 0
    for m in range(n):
        ansi += p[m][l[m]]
    ans = max(ans,ansi)
print(ans)