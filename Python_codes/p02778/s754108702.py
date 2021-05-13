import re

s = str(input())

print(re.sub('[a-z]', 'x', s))