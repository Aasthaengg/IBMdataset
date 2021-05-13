# 初期入力
import sys
input = sys.stdin.readline
A,B = (int(i) for i in input().split())
if (B/A).is_integer() :
    print(A+B)
else:
    print(B-A)