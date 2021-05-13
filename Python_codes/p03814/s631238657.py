s = input()
a = len(s)
b = 0
for i in range(len(s)):
  if s[i] == "A":
    a = min(a, i)
  if s[i] == "Z":
    b = max(b,i)
res = b-a+1
print(res)