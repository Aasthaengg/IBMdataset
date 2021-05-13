S = list(input())
USED = [False] * 26

for s in S:
  USED[ord(s)-97] = True
  
ok = False
ans = None
for i in range(26):
  if not USED[i]:
    ans = chr(97+i)
    ok = True
    break
    
if ok:
  print(ans)
else:
  print("None")
