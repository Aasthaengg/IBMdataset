import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())

ans = [-1]*N
for i in range(N-1, -1, -1):
    a = As[i]
    idx = i+1
    if idx*2>N:
        ans[i] = a
        continue
    cnt = 2
    per = 0
    while cnt*idx<=N:
        per += ans[cnt*idx-1]
        cnt += 1
    per %= 2
    ans[i] = 1 if per!=a else 0
print(sum(ans))
if sum(ans):
    print(*[i+1 for i, x in enumerate(ans) if x!=0])