s = input()

if s[0] == 'A' and s[2:-1].count('C') == 1:
    t = s[1:].replace('C', '')
    ans = 'AC' if t.lower() == t else 'WA'
else:
    ans = 'WA'

print(ans)