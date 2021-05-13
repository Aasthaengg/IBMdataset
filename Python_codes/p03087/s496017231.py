import sys
readline = sys.stdin.readline

N,Q = map(int,readline().split())
S = readline().rstrip()

cnt = [0] * (N + 1)
for i in range(1,len(S)):
  if S[i - 1:i + 1] == "AC":
    cnt[i + 1] = 1
    
for i in range(1,len(cnt)):
  cnt[i] = cnt[i - 1] + cnt[i]
  
for i in range(Q):
  l,r = map(int,readline().split())
  print(cnt[r] - cnt[l])
