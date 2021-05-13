MOD = 10 ** 9 + 7
INF = 10 ** 11
import sys
sys.setrecursionlimit(100000000)

N,A,B,C = map(int,input().split())
L = [int(input()) for _ in range(N)]

ans = INF
def dfs(i,before,score):
    global ans
    if i == N:
        if all(length > 0  for length in before):
            x,y,z = before
            for _ in range(3):
                ans = min(ans,abs(x - A) + abs(y - B) + abs(z - C) + score - 30)
                x,y,z = y,z,x
    else:
        dfs(i + 1,before,score)
        for j in range(3):
            before[j] += L[i]
            dfs(i + 1,before,score + 10)
            before[j] -= L[i]
dfs(0,[0,0,0],0)
print(ans)