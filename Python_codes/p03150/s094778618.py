s = input()
ans_flag = False
if "keyence" in s:
  ans_flag = True
  
t = "keyence"
for i in range(1,7):
  first_half = t[:i]
  second_half = t[i:]
  if first_half == s[:len(first_half)]:
    if s[-len(second_half):] == second_half:
      ans_flag = True

print("YES" if ans_flag else "NO")