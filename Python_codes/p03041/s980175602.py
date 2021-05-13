n,k = map(int,input().split())
s = input()
ans = ''

for p in range(len(s)):
  if p == k - 1:
    if s[p] == 'A':
      ans += 'a'
    elif s[p] == 'B':
      ans += 'b'
    elif s[p] == 'C':
      ans += 'c'
  else:
    ans += s[p]
    
print(ans)