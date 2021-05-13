s = input()

ans = 0
for i in range(1, len(s)):
  tmp_s = s[: - i]
  tmp_N = len(tmp_s)
  if tmp_N % 2 == 1:
    continue
  tmp_s_l = tmp_s[:tmp_N//2]
  tmp_s_r = tmp_s[tmp_N//2:]
  if tmp_s_l == tmp_s_r:
    ans = tmp_N
    break

print(ans)
