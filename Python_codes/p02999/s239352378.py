import sys
input = sys.stdin.readline

X,A =list(map(int,input().split()))
print(10 if A <= X else 0)
