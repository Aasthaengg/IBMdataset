s = input()
ans = 0
for i in range(0,3,2):
  if s[i] == "0" and s[i+1] == "0":
    continue
  elif s[i] == "0":
    ans += i+1
  elif (s[i] == "1" and s[i+1] == "0") or (s[i] == "1" and s[i+1] == "1") or (s[i] == "1" and s[i+1] == "2"):
    ans += i+1
if ans == 1:
  print("MMYY")
elif ans == 3:
  print("YYMM")
elif ans == 4:
  print("AMBIGUOUS")
else:
  print("NA")