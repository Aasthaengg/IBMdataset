import re
n = int(input())
s = input()
m = re.findall("ABC", s)
print(len(m))
