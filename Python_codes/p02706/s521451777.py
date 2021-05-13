sv,m = input().split(" ") # 夏休みの日数と問題数を数値で格納
sv = int(sv)
m = int(m)

day = input().split(" ") #
days = 0 #

for i, new in enumerate(day): # 独学のP105をパクる
    days += int(day[i]) # 宿題を終わらせるのにかかる総日数を加算で出す

if days > sv: # 総日数が夏休み日数より多かったら-1を出力
    print("-1")
else: # じゃなかったら残り日数を遊べる日として出力
    print(sv - days)
