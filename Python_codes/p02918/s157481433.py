
N, K = map(int, input().split())
S = list(input()+"X")

temp = S[0]
cnt = 1
c_cnt = 1
ans = 0

for i in range(1, N+1):
  if temp == S[i]:
    cnt += 1
  else:
    ans += cnt - 1
    cnt = 1
    c_cnt += 1
    temp = S[i]
  #print(ans, cnt, c_cnt, temp)

#最後の余計な分
c_cnt -= 1

if c_cnt//2 <= K:
  if c_cnt%2 == 0:
    ans += (c_cnt//2) * 2 - 1
  else:
    ans += (c_cnt//2) * 2
else:
  ans += K * 2

print(ans)