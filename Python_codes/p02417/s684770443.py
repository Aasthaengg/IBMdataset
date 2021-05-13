alpha = [chr(i) for i in range(97, 97+26)]

import sys
s = " "
for line in sys.stdin:
    s += line.lower()

for i in s:
    if i.lower() in alpha:
        alpha.append(i.lower())
        
for i in alpha[:26]:
    print(str(i) + " : " + str(alpha.count(i) - 1))      