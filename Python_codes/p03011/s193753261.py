# 数値を取得
time_list = list(map(int,input().split()))

# 最短時間を出力
time_list = sorted(time_list)
sumtime = time_list[0] + time_list[1]
print(sumtime)