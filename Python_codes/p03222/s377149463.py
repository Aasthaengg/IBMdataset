H,W,K = map(int, input().split())

# dp[h][w]
dp = []
for _ in range(H+1):
    dp.append([0] * W)

dp[0][0] = 1

for h in range(1,H+1):
    for w in range(0,W):
        a = 0
        b = 0
        c = 0
        
        Q = W-1
        for bit in range(1<<Q):
            invalid = False
            cur_seq = False
            for i in range(Q):
                on = (bit >> i) & 1
                if on & cur_seq:
                    invalid = True
                    break
                cur_seq = on

            # if there is sequential bar, then the combination is invalid
            if invalid:
                continue

            connected = False
            # if the combination has connection with w then count a or c
            # otherwise, inc b
            for i in range(Q):
                on = (bit >> i) & 1
                if on:
                    x = i
                    y = i+1
                    if x == w-1:
                        connected = True
                        a += 1
                    elif y == w+1:
                        connected = True
                        c += 1
            if not connected:
                b += 1

        cnt = 0
        if a > 0:
            cnt += a * dp[h-1][w-1]
        if b > 0:
            cnt += b * dp[h-1][w]
        if c > 0:
            cnt += c * dp[h-1][w+1]

        dp[h][w] = cnt

print(dp[H][K-1] % 1000000007)