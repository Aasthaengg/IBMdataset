import sys
input = sys.stdin.readline
X,t = [int(i) for i in input().split()]
if X <= t :
    print(0)
else :
    print(X-t)