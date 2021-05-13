import sys
import bisect
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
x = int(readline())

if x >= 1200:
    print("ARC")
else:
    print("ABC")