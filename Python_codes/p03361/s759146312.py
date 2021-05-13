h, w = map(int, input().split())
# H行受け取る
ab = list(input() for _ in range(h))
# (h+2)*(w+2)、indexは0,1,...,h+1(or w+1)で、考えるのは1,2,...,h(or w)
dp = [["_" for i in range(w + 2)] for j in range(h + 2)]

for i in range(h):
    for j in range(w):
        dp[i + 1][j + 1] = ab[i][j]

for i in range(h):
    for j in range(w):
        if dp[i + 1][j + 1] == "#":
            # 四方の少なくとも一つが#ならOK
            if dp[i][j + 1] == "#" or dp[i + 2][j + 1] == "#" or dp[i + 1][j] == "#" or dp[i + 1][j + 2] == "#":
                pass
            # そうでない場合は塗ることはできない
            else:
                print("No")
                exit()

print("Yes")
