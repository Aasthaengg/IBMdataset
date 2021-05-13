import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
    
if X % Y == 0:
    print(-1)
    exit()

print(X)