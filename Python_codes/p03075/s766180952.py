# 初期入力
import sys
input = sys.stdin.readline
a =[]
for i in range(5):
    x = int(input())
    a.append(x)
k = int(input())

#ソートして最大と最小を比較
if a[-1] -a[0] >k:
    print(":(")
else:
    print("Yay!")