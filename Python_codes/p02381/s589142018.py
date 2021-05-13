import math

# 標準偏差を求める
def standard_deviation():
    average = sum(s) / n  # 平均値を求める
    total_deviation = 0
    for element in s:
        total_deviation += (element - average)**2 # 偏差の合計を求める

    return math.sqrt(total_deviation / n) # 標準偏差を求める


while True:
    n = int(input())
    if n == 0: break
    s = [int(s) for s in input().split()]
    print('{0:.5f}'.format(standard_deviation()))
