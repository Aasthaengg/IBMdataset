import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = int(readline())
ans = 10**18
for i in range(1,n):
    j = n-i
    s = str(i).rjust(6,"0")[::-1]
    t = str(j).rjust(6,"0")[::-1]
    res = 0
    for i,j in zip(s,t):
        res += int(i)+int(j)
    ans = min(res,ans)

print(ans)

