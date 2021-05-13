N = int(input())
s = input()
if N < 2:
  result = "No"
else:
  n = int(N/2)
  s1 = s[:n]
  s2 = s[n:]
  if s1 == s2:
    result = "Yes"
  else:
    result = "No"
print(result)