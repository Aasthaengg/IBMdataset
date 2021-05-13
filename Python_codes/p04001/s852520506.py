import sys

readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prl = lambda x: print(*x ,sep='\n')

s = ns()
ans = 0
n = len(s)
t = 2**(n-1)
for i in range(t):
    moji = list(s)
    for j in range(n):
        if (i >> j) & 1:
            moji.insert(n-j-1,'+')
    ans += eval(''.join(moji))
print(ans)