import re
s = input()
s = re.sub('[W]+', 'W', s)
s = re.sub('[B]+', 'B', s)
ans = len(s) - 1
print(ans)