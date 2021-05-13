import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


h,w,d = list(map(int, input().split()))
a = [None]*h
n = h*w
dd = [None]*(n)
for i in range(h):
    a[i] = list(map(int, input().split()))
    for j,num in enumerate(a[i]):
        dd[num-1] = (i,j)
vals = [[] for _ in range(d)]
for i in range(d):
    l = []
    prev = i
    s = 0
    for j in range(i, n, d):
        v = abs(dd[j][0]-dd[prev][0]) + abs(dd[j][1]-dd[prev][1])
        s += v
        l.append(s)
        prev = j
    vals[i] = l
q = int(input())
ans = [None]*q
for i in range(q):
    ll,rr = map(lambda x: int(x)-1, input().split())
    ans[i] = vals[rr%d][rr//d] - vals[ll%d][ll//d]
write("\n".join(map(str, ans)))