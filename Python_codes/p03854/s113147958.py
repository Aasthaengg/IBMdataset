s = input()

tmp = ""
cnt = 0
for c in reversed(s):
  tmp = c + tmp
  if tmp in ["dream", "dreamer", "erase", "eraser"]:
    cnt += len(tmp)
    tmp = ""
    
if cnt == len(s):
  print("YES")
else:
  print("NO")