h,w,k = map(int,input().split())


#dp[h][k]
bits = []
for i in range(2**(w-1)):
    bit = [0] * (w-1)
    for j in range(w-1):
        if ((i >> j) & 1):
            bit[j] = 1
    for j in range(w-2):
        if bit[j] == 1 and bit[j+1] == 1:
            break
    else:
        bits.append(bit)

path = [[0 for i in range(w)] for i in range(w)]

for bit in bits:
    for ww in range(w):
        flag = True
        if ww != w-1:
            if bit[ww] == 1:
                flag = False
                path[ww][ww+1] += 1
        if ww != 0:
            if bit[ww-1] == 1:
                flag = False
                path[ww][ww-1] += 1
        if flag:
            path[ww][ww] += 1

            
dp = [[0 for ww in range(w)] for hh in range(h+1)]

dp[0][0] = 1

for hh in range(h):
    for ww in range(w):
        for ww2 in range(w):
            dp[hh+1][ww2] += dp[hh][ww] * path[ww][ww2] 
            dp[hh+1][ww2] %= 1000000007
            
print(dp[-1][k-1])