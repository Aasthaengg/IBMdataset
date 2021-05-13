import sys
readline = sys.stdin.buffer.readline

n = int(readline())
t,a = 0,0
for i in range(n):
    rt,ra = map(int,readline().split())
    x = max((t-1)//rt+1,(a-1)//ra+1)
    t = rt*x
    a = ra*x
    if a+t == 0:
        t += rt
        a += ra

print(t+a)

