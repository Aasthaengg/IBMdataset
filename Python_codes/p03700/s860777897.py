import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,a,b = map(int, input().split())
hs = [None]*n
for i in range(n):
    hs[i] = int(input())
    
def sub(x):
    vs = [max(item - b*x, 0) for item in hs]
    return sum(v // (a-b) + bool(v % (a-b)) for v in vs) <= x

l = 0
r = 10**9

while l<r-1:
    m = (l+r)//2
    if sub(m):
        r = m
    else:
        l = m
print(r)