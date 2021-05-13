s_str = input()
s_list = list(s_str)
g_count = 0
p_count = 0
score = 0
for s in s_list:
  if p_count >= g_count:
    if s == "p":
      score -= 1
    g_count += 1
  else:
    if s == "g":
      score += 1
    p_count += 1
print(score)