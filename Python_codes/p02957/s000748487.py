# 初期入力
import sys
input = sys.stdin.readline
A,B = (int(x) for x in input().split())
diff = A-B
if diff %2 ==1:
    print("IMPOSSIBLE")
else:
    print((A+B)//2)