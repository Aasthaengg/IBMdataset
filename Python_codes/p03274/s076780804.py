import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k = map(int, readline().split())
x = list(map(int, readline().split()))
p = []
m = [0]
for i, xx in enumerate(x):
    if xx > 0:
        m += x[i:]
        break
    p.append(abs(xx))
p = [0] + p[::-1]
sizep = len(p) - 1
sizem = len(m) - 1
ans = float('inf')
for i in range(k):
    pp = k - i
    mm = i
    if sizep < pp:
        mm += pp - sizep
        pp = sizep
    if sizem < mm:
        pp += mm - sizem
        mm = sizem
    v = p[pp] + m[mm]
    if pp != 0 and mm != 0:
        v += min(p[pp], m[mm])
    ans = min(ans, v)
print(ans)
