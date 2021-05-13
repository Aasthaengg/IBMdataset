s = input()
t = input()
sw = s*2
for i in range(len(s)):
  if sw[i:i+len(s)] == t:
    print("Yes")
    break
else:
  print("No")