import sys

readline = sys.stdin.readline
readlines = sys.stdin.readlines
ns = lambda: readline().rstrip() # input string
ni = lambda: int(readline().rstrip()) # input int
nm = lambda: map(int, readline().split()) # input multiple int 
nl = lambda: list(map(int, readline().split())) # input multiple int to list

a, b, x = nm()
d_min = x - (a % x)
if d_min == x: 
    d_min = 0
d_max = b % x
min = a + d_min
max = b - d_max
if min > max: 
    ans = 0
else:
    ans = ((max - min) // x + 1)
print(ans)