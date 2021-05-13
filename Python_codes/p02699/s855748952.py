import sys
input = sys.stdin.readline

S,W = list(map(int,input().split()))

print('safe' if S>W else 'unsafe')
