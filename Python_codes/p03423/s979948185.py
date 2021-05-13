import sys
input = sys.stdin.readline
N = int(input())
if N < 3 :
    print(0)
else :
    print(N//3)