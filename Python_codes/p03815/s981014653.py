import sys
import bisect
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
x = int(readline())

res,mod = divmod(x,11)
res*=2
if mod == 0:
    print(res)
elif mod <= 6:
    print(res+1)
else:
    print(res+2)