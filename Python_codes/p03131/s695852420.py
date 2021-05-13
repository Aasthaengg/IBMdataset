import sys
input = sys.stdin.readline
# int(input()) # 入力が1つ
k, a, b = map(int, input().split()) # 入力が複数
# [int(i) for i in input().split()] # 配列で数字

bis = 1
m = 0
if b - a < 2:
    print(bis + k)
else:
    change = (k - (a - 1)) // 2
    bis += k - change * 2
    bis += change * (b - a)
    print(bis)