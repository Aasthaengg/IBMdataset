# 初期入力
import sys
input = sys.stdin.readline
A,B = (int(i) for i in input().split())
if 13 <= A:
    ans =B
elif 6 <= A <=12:
    ans =B//2
elif A <=5:
    ans =0

print(ans)