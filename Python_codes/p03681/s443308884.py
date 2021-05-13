import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,m = list(map(int, input().split()))
M = 10**9+7
if abs(n-m)>=2:
    val = 0
else:
    val = 1
    for i in range(1,n+1):
        val *= i
        val %= M
    for j in range(1,m+1):
        val *= j
        val %= M
    if abs(n-m)==0:
        val *= 2
        val %= M
print(val)