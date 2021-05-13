# 初期入力
import sys
input = sys.stdin.readline
A,B,T = (int(x) for x in input().split())
num =(T +0.5)//A
ans =B *num
print(int(ans))