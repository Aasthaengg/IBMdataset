import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

K = int(input())

ans = set()
def dfs(last, lis):
    ans.add(int(''.join(lis)))
    if len(lis)==11:
        return
    dfs(last, lis+str(last))
    if last!=0:
        dfs(last-1, lis+str(last-1))
    if last!=9:
        dfs(last+1, lis+str(last+1))

for i in range(1, 10):
    dfs(i, str(i))

ans = list(ans)
ans.sort()
print(ans[K-1])