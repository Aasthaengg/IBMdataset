s = input()
t = input()
if len(s) < len(t):
  print("UNRESTORABLE")
  exit()

start = -1
for i in range(len(s)-len(t)+1):
  for j in range(len(t)):
    if s[i+j] != "?" and s[i+j] != t[j]:
      break
  else:
    start = i

if start == -1:
  print("UNRESTORABLE")
else:
  ans_list = list(s)
  for i in range(len(ans_list)):
    if start <= i < start+len(t):
      ans_list[i] = t[i-start]
    elif ans_list[i] == "?":
      ans_list[i] = "a"
  print("".join(ans_list))
    
    
