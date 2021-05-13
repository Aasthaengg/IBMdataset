# 初期入力
import sys
input = sys.stdin.readline
H,W = (int(i) for i in input().split())
h,w = (int(i) for i in input().split())
common =h*w
ans = H*W -h*W -H*w +common
print(ans)