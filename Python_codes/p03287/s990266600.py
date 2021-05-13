import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,m = list(map(int, input().split()))
a = list(map(int, input().split()))
def cumsum(a):
    """※ aを破壊する
    l[i] = sum(a[:i]) なるlを返す
    sum(a[i:j]) == l[j+1] - l[i]
    """
    c = 0
    n = len(a)
    a.insert(0, 0)
    for i in range(1, n+1):
        a[i] = a[i-1]+a[i]
    return a
cumsum(a)
from collections import Counter
c = Counter([(item%m) for item in a])
ans = sum((v*(v-1)//2) for v in c.values())
print(ans)