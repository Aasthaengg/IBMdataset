s = str(input())
for i in range(len(s)):
  if s[i] == 'A':
    start = i
    break
for i in range(len(s)):
  if s[len(s)-1-i] == 'Z':
    stop = len(s)-i
    break
ans = stop-start
print(ans)