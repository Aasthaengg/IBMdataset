s = input()
n = len(s)
if s[0:n] == s[::-1]:
  if s[0:(n-1)//2] == s[(n+1)//2:n]:
    print("Yes")
  else:
    print("No")
else:
  print("No")