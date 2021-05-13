# 初期入力
import sys
import math
input = sys.stdin.readline
N = int(input())
a_max =[] #移動手段の最大乗車人数
num =[0]*5 #各移動機関の稼働回数
for i in range(5):
    x = int(input())
    a_max.append(x)
    num[i] =math.ceil(N /x)

#ボトルネックを過ぎれば、時間は距離に比例
max_value = max(num)
max_index = num.index(max_value)
ans =num[max_index] +6-2
print(ans)