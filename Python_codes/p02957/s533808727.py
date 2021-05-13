import sys
input = sys.stdin.readline

A,B = list(map(int,input().split()))
print('IMPOSSIBLE' if (A+B)/2 != int((A+B)/2) else (A+B)//2)
