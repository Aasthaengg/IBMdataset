import sys
input = sys.stdin.readline

if sum(list(map(int, input().split()))) >= 22:
    print("bust")
else:
    print("win")