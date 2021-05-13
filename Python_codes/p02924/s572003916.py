# https://atcoder.jp/contests/abc139/tasks/abc139_d
# math
import sys
input = sys.stdin.readline
n = int(input()) # 入力が1つ
# map(int, input().split()) # 入力が複数
# ans = 0
# for i in range(n):
#     ans += i
# print(ans)

ans = (n + 1) * n // 2 - n
print(ans)