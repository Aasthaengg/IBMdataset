n = int(input())
s = str(input())
t = str(input())
for i in range (n+1):
  b = s[0:i] + t[0:n]
  if b[0:n] == s:
    n += i
    break
print(n)