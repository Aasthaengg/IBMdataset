n = int(input())
s = input()
m = 0
for i in range(1, n-1):
  if m < len(list(set(s[:i]) & set(s[i:]))):
    m = len(list(set(s[:i]) & set(s[i:])))
print(m)