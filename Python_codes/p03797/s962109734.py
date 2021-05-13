#55c
N,M = map(int, input().split())

ans = 0

#まずSのピースを使い果たす。
made_scc = min(N,int(M/2))
ans += made_scc
#N -= made_scc
M -= 2 * made_scc
#cのピースを使い果たす。
ans += int(M/4)

print(ans)