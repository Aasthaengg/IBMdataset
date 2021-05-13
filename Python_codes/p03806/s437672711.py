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
    def sub(v1, v2, i, bound, ll, ind=0):
        if i==bound:
            ll.append((v1,v2))
            return
        sub(v1, v2, i+1, bound, ll, ind)
        sub(v1+l[ind+i][0], v2+l[ind+i][1], i+1, bound, ll, ind)
    sub(0, 0, 0, n1, l1)
    sub(0, 0, 0, n2, l2, ind=n1)
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
    if v==0 and c>0:
        ans = min(ans, c)
for v,c in l2:
    if v==0 and c>0:
        ans = min(ans, c)
        
for v,c in l1:
    if -v in d2 and c+d2[-v]>0:
        ans = min(ans, c+d2[-v])
if ans == float("inf"):
    ans = -1
print(ans)