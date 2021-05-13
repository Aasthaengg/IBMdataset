s = input()
flag = False
r = "keyence"
for i in range(len(s)):
  #print(s[:i+1], r[:i+1])
  #print(s[len(s)-len(r[i+1:]):], r[i+1:])
  if s[:i+1] == r[:i+1] and s[len(s)-len(r[i+1:]):] == r[i+1:]:
    flag = True
    break
if flag:
  print("YES")
else:
  print("NO")
    
