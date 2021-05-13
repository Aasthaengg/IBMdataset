N = int(input())
a = list(map(int, input().split()))

# 最小の答えは1、ここに足していく
ans = 1

# 増加と減少切り替わったタイミングで組の数を増やす
flags = [False, False]

for i in range(N - 1):
    da = a[i + 1] - a[i]
    if da > 0:
        flags[0] = True
    elif da < 0:
        flags[1] = True

    if flags[0] == True and flags[1] == True:
        ans += 1
        # 初期化
        flags = [False, False]

print(ans)
