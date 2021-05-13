n = int(input())
As = [int(input()) for i in range(n)]
dp  = [0] * n #どこまで伸ばせたか
mx = 0
prev = 0
for i,a in enumerate(As):
    if a == 0:continue
    # prev + 1より大きくなることはありえない
    if prev + 1 < a:
        print(-1)
        exit()
    if i - a < mx: #遡ってしまったら
        print(-1)
        exit()
    else:
        dp[i-a] = a
        mx = i-a
    prev = a
print(sum(dp))    