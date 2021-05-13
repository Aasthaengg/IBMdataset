N,Q =map(int,input().split())
S = input()
lr = [list(map(int,input().split())) for _ in range(Q)]

ans = 0
ans_ls = []
ans_ls.append(0)

for n in range(N-1):
  if S[n] == "A" and S[n+1] =="C":
    ans += 1
  ans_ls.append(ans)

for q in range(Q):
  print(ans_ls[lr[q][1]-1]-ans_ls[lr[q][0]-1])
