S=input()
p = 'a'
for s in S:
  if p == s:
    p = 'a'
    break
  else:
    p = s
print("Bad" if p == 'a' else "Good")