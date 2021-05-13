import re
s = input()
s = s[::-1]
#print(s)
match = re.match('((remaerd)|(maerd)|(resare)|(esare))*',s)
#print(match)
#print(match.group())
if match.group() == s:
    print('YES')
else:
    print('NO')