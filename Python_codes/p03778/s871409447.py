import sys
import bisect
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
w,a,b = map(int,readline().split())

if a > b:
    a,b = b,a

print(max(0,b-(a+w)))