N, K = map(int, input().split())
S = list(input())
T = []
pre = S[0]
cnt = 0
ans = -1
for i in range(N):
  if S[i] == pre:
    cnt += 1
    pass
  else:
    T += [pre]
    ans += cnt
    cnt = 0
    pre = S[i]

ans += cnt
T += [pre]
ans += min(K*2, len(T)-1)
print(ans)