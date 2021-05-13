s = input()

while len(s) > 7:
  if s[-5:] in ["dream", "erase"]:
    s = s[:-5]
  elif s[-6:] in ["eraser"]:
    s = s[:-6]
  elif s[-7:] in ["dreamer"]:
    s = s[:-7]
  else:
    break

if (len(s)==5 and s in ["dream", "erase"]) or (len(s)==6 and s in ["eraser"]) or (len(s)==7 and s in ["dreamer"]):
  print("YES")
else:
  print("NO")