n = int(input())
s = input()
ans = 0

for i in range(1, n):
  cmn = set(s[:i]) & set(s[i:])
  ans = max(ans, len(cmn))
  
print(ans)