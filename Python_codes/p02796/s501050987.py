n = int(input())

xl = [list(map(int, input().split())) for _ in range(n)]

# 計算しやすいように区間を出しておく
position = [(xl[i][0]-xl[i][1],xl[i][0]+xl[i][1]) for i in range(n)]
position = sorted(position, key=lambda x: x[1])

min_arm = -float('inf')
ans = 0

# 全ロボットを見る
for pos in position:
    # 腕が交わらない場合
    if  min_arm <= pos[0]:
        ans += 1
        min_arm = pos[1]
print(ans)