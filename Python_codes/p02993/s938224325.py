s = input()
before = s[0]
for i in range(1,len(s)):
  if before == s[i]:
    print('Bad')
    exit()
  before = s[i]
print('Good')