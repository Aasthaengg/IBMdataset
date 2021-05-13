s = input()
ans = 'AC'
if s[0] != 'A':
    ans = 'WA'
if not('C' in s[2:-1]):
    ans = 'WA'
s = s.replace('A','')
s = s.replace('C','',1)
for i in s:
    if ord(i) < ord('a') or ord(i) > ord('z'):
        ans = 'WA'
print(ans)
