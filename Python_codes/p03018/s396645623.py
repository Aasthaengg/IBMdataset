s = input()
a = 0
ans = 0
n = len(s)
i = 0
while(i<n):
  if s[i] == "A":
    a += 1
  elif s[i] == "B" and i+1<n and s[i+1] == "C":
    ans += a
    i += 1
  else:
    a = 0
  i += 1
print(ans)