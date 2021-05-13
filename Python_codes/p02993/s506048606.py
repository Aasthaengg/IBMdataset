s = input()
bad = 0
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        bad = 1
        break

if bad:
    print('Bad')
else:
    print('Good')