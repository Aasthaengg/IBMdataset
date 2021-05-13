N, K = map(int, input().split())
S = list(input())
r_cnt = 0
answer = 0
before = S[0]
for s in S:
  if s == before:
    answer += 1
  else:
    r_cnt += 1
    before = s
answer -= 1
if r_cnt%2 == 0:
  print(answer+min(r_cnt//2, K)*2)
elif r_cnt//2 >= K:
  print(answer+K*2)
else:
  print(answer+(r_cnt//2+1)*2-1)
