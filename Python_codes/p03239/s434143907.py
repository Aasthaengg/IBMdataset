# 問題文をよく読みましょう
n,m = map(int, input().split())
cost, time = 10000, 10000
for i in range(n):
    c,t = map(int, input().split())
    # 時間がmより小さい
    if m >= t:
            cost = min(cost,c)
            
if cost == 10000:
    print('TLE')
else:
    print(cost)
