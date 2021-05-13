import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
mod = 10**9 + 7


def perm(n, k):
    if k == 0:
        return 1
    return n * perm(n-1, k-1) % mod


n, k = map(int, input().split())
child = [0] * n

for _ in range(n-1):
    a, b = map(lambda x: int(x)-1, input().split())
    child[a] += 1
    child[b] += 1

ans = k
for i in range(n):
    if i == 0:
        color = k - 1
        num = child[i]
    else:
        color = k - 2
        num = child[i] - 1
    ans = ans * perm(color, num) % mod

print(ans)