n = int(input())
H = list(map(int, input().split()))

# シミュレーションで求められる
# 目標地点からさかのぼる

ans = 0
for _ in range(max(H)):
    flg = False
    for i in range(n):
        if H[i] > 0:
            H[i] -= 1
            if not flg:
                ans += 1
                flg = True
        elif H[i] == 0:
            flg = False

print(ans)