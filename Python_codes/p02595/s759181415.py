
import sys
import math
input = sys.stdin.readline

def inlt():
    return(list(map(int,input().split())))
n, d = inlt()
cnt = 0
for i in range(n):
    x, y = inlt()
    if math.sqrt(x**2+y**2)<=d:
        cnt+=1
print(cnt)        