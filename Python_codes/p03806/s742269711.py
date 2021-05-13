import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n, ma, mb = list(map(int, input().split()))
abc = [None]*n
for i in range(n):
    a,b,c = tuple(map(int, input().split()))
    abc[i] = (a*mb - b*ma, c)
abc.sort()
def halfcomb(l):
    n = len(l)
    n1 = n//2
    n2 = (n+1)//2
    l1 = []
    l2 = []
    
    for b in range(1, 1<<n2):
        v11, v12 = 0, 0
        v21, v22 = 0, 0
        for i in range(n2):
            if b&1<<i:
                item = l[n1+i]
                v21+=item[0]
                v22+=item[1]
                if b<(1<<n1) and i<n1:
                    item = l[i]
                    v11+=item[0]
                    v12+=item[1]
        if b<(1<<n1):
            l1.append((v11,v12))
        l2.append((v21,v22))
    return l1, l2
l1, l2 = halfcomb(abc)
d2 = {}
for v,c in l2:
    if v in d2:
        d2[v] = min(d2[v], c)
    else:
        d2[v] = c
ans = float("inf")
for v,c in l1:
    if v==0:
        ans = min(ans, c)
for v,c in l2:
    if v==0:
        ans = min(ans, c)
        
for v,c in l1:
    if -v in d2:
        ans = min(ans, c+d2[-v])
if ans == float("inf"):
    ans = -1
print(ans)