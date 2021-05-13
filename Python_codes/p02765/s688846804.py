import sys
input = sys.stdin.readline
# int(input()) # 入力が1つ
n, r = map(int, input().split()) # 入力が複数
# [int(i) for i in input().split()] # 配列で数字

if n >= 10:
    print(r)
else:
    print(r + 100 * (10 - n))