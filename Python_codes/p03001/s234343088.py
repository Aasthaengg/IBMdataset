# 初期入力
import sys
input = sys.stdin.readline
W,H,x,y = (int(x) for x in input().split())
ans1 =0
ans2 =0
if W/2 ==x and H/2 ==y:
    ans2= 1
else:
    ans2 =0
ans1 =W *H/2
print(ans1,ans2)