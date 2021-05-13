N, K = map(int, input().split())			# "5 7" -> ["5", "7"] -> 5, 7 => N=5,K=7

ans = max(0, N-K)

if K==1: ans=0

print(ans)
