import re
n = input()
m = re.search('(\d+)\s(\d+)', n)
a = int(m.group(1))
b = int(m.group(2))
i = 0
if a < b:
    i += b
    b -= 1
    if a < b:
        i += b
        print(i)
    else:
        i += a
        print(i)
else:
    i += a
    a -= 1
    if a < b:
        i += b
        print(i)
    else:
        i += a
        print(i)
