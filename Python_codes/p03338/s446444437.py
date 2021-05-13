n = int(input())
s = input()
res = 0
for i in range(n):
  res = max(res, len(set(s[:i]) & set(s[i:])))
print(res)