import sys
import bisect
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
a,b,c = map(int,readline().split())

if  a <= b <= c or a >= b >= c:
    if abs(a-b)==abs(b-c):
        print("YES")
        exit()
print("NO")