import re
s=input()
print(re.sub(r'[0-9]{4}/([0-9]{2})/([0-9]{2})',r'2018/\1/\2',s))
