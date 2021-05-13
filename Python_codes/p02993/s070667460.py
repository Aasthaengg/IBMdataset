s = input()
ans = False
for i in range(3):
  if s[i] == s[i + 1]:
    ans = True
    break
print("Bad" if ans else "Good")