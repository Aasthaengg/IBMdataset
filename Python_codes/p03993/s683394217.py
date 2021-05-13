import sys

readline = sys.stdin.readline
readlines = sys.stdin.readlines
ns = lambda: readline().rstrip() # input string
ni = lambda: int(readline().rstrip()) # input int
nm = lambda: map(int, readline().split()) # input multiple int 
nl = lambda: list(map(int, readline().split())) # input multiple int to list

n = ni()
l = nl()
ans = 0

for i, usa in enumerate(l):
    if l[usa - 1] == i + 1:
        ans += 1
print(ans // 2)