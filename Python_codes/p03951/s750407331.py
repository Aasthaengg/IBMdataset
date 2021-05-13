N = int(input())
s = input()
t = input()

if s == t:
  print(N)
  exit(0)

cnt = 0
for i in range(N):
  tmp_s = s[i:]
  tmp_t = t if i == 0 else t[:-i]

  tmp_cnt = 0
  for j in range(len(tmp_s)):
    if tmp_s[j] == tmp_t[j]:
      tmp_cnt += 1

  cnt = max(cnt, tmp_cnt)

print(2 * N - cnt)
