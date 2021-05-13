# 初期入力
import sys
input = sys.stdin.readline
X,A = (int(x) for x in input().split())
if A <= X:
    print(10)
else:
    print(0)