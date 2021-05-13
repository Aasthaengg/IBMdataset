import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")



q = int(input())
lr = [None]*q
for i in range(q):
    lr[i] = tuple(map(int, input().split()))
n = max(item[1] for item in lr) + 10

def hurui(n):
    """n以下の素数のリストを返す
    """
    l = list(range(2,n+1))
    p = 2
    i = 0
    while True:
        l = [item for item in l if item==p or item%p!=0]
        i += 1
        p = l[i]
        if p*p>n:
            break
    return l
l = hurui(n)
l = set(l)
v = [0]*n # 0, 1, ..., iのうちの個数
c = 0
for i in range(n):
    if i%2==1 and i in l and (i+1)//2 in l:
        c += 1
    v[i] = c
ans = []
for l,r in lr:
    ans.append(v[r]-v[l-1])
write("\n".join(map(str, ans)))