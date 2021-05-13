import sys
input = sys.stdin.readline

s = list(input().strip())
r = s.count('0')
b = s.count('1')
print(2*min(r,b))