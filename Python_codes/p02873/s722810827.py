s = input()
right_cnt = 0
left_cnt = 0
total = 0
for i in range(len(s)):
  if s[i] == '<' and left_cnt == 0:
    right_cnt += 1
  elif s[i] == '<' and left_cnt > 0:
    k = max(right_cnt, left_cnt)
    l = min(right_cnt, left_cnt)
    total += (((k+1)*k) + (l*(l-1)))//2
    right_cnt = 1
    left_cnt = 0
  elif s[i] == '>':
    left_cnt += 1
k = max(right_cnt, left_cnt)
l = min(right_cnt, left_cnt)
total += (((k+1)*k) + (l*(l-1)))//2
print(total)
