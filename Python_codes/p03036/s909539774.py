# 初期入力
import sys
input = sys.stdin.readline
r,D,x2000 = (int(i) for i in input().split())
x =[0]*11
x[0] =x2000
for i in range(10):
    x[i+1] =r*x[i] -D
    print(x[i+1])