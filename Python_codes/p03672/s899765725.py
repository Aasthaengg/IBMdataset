s = input()
ans = 0
for i in range(1,len(s)//2):
  if s[:i] == s[i:2*i]: ans = i * 2
print(ans)