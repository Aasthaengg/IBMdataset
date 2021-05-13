import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n,m = map(int,readline().split())
lst1 = []
for i in range(n):
    lst1.append(list(map(int,readline().split())))

ans = 0
for i in range(1<<4):
    res = [0]*n
    for j in range(3):
        if i>>j&1:
            for k in range(n):
                res[k] += lst1[k][j]
        else:
            for k in range(n):
                res[k] -= lst1[k][j]
    res.sort(reverse=True)
    ans = max(ans,sum(res[:m]))

print(ans)
