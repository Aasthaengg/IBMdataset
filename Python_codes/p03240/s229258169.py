# 参考:https://atcoder.jp/contests/abc112/submissions/14491766
import sys
input = lambda: sys.stdin.readline().rstrip()
 
l = []
for _ in range(int(input())):
    t = list(map(int,input().split()))
    l.append(t)
    if t[2]: 
        x,y,h = t[0], t[1], t[2]
        
for X in range(101):
    for Y in range(101):
        H = h + abs(x - X) + abs(y - Y)
        if all(h==max(H - abs(x-X) - abs(y-Y), 0) for x,y,h in l): print(X, Y, H)