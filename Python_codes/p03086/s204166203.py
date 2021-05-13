s = str(input())
n = len(s)
ans,ch = 0,0
for i in range(n):
  if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
    ch += 1
  else:
    ch = 0
  if ch >= ans:
    ans = ch
print(ans)