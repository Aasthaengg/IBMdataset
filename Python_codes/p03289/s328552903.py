s = input()
ans = 'WA'
if s[0] == 'A' and s[2:len(s)-1].count('C') == 1:
  s = s.replace('A', '').replace('C', '')
  if all([i in [chr(i) for i in range(97, 97+26)] for i in s]):
    ans = 'AC'
print(ans)