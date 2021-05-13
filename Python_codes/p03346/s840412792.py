import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())

Q = [0]*N
for i in range(N):
    p = int(input())
    Q[p-1] = i

cnt = 0
now_idx = -1
ans = 0
for i in range(N):
    idx = Q[i]
    if idx>now_idx:
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 1
    now_idx = idx

print(N-ans)