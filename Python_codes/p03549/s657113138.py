n,m = map(int,input().split())
# 1ケースでかかる時間を求める
total = m*1900 + (n-m)*100
# 全てのケースで正解する確率の分母
prob_all = 2**m
print(total * prob_all)