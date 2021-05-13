import sys
input = sys.stdin.readline
# int(input()) # 入力が1つ
a, p = map(int, input().split()) # 入力が複数
# [int(i) for i in input().split()] # 配列で数字

ans = (a * 3 + p) // 2
print(ans)