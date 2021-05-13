s=str(input())
d=True
for i in range(3):
  if s[i+1]==s[i]:
    d=False
    
if d:
  print("Good")
else:
  print("Bad")