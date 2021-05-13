#AGC029-A Irreversible operation
"""
問題：
一直線上にオセロがある
一回の操作で[黒白]を裏返す時[白黒]、最大何回の操作が行えるか
解法：
まずいちばん最初のBが出てくるところまでは無視できる
そこから、Wが出てくる度にそこまでに出現したBの数を足した合計が答え
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
s = readline().rstrip().decode('utf-8')
flag = 0
black = 0
white = 0
ans = 0
for i in s:
    if flag:
        if i == "B":
            black += 1
        else:
            ans += black
    else:
        if i == "B":
            flag = 1
            black += 1
print(ans)