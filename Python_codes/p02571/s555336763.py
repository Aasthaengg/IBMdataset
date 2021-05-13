s = input().rstrip()
t = input().rstrip()
l_s = len(s)
l_t = len(t)
ans = l_t
for i in range(l_s-l_t+1):
  tmp_ans = l_t
  for j in range(l_t):
    if t[j] == s[i+j]:
      tmp_ans -= 1
  ans = min(ans, tmp_ans)
print(ans)