import re
S = input()
s = set(S)
m = re.findall(S[0],S)
m

if len(s) == 2:
    if len(m) == 2:
        print('Yes')
        exit()
print('No')
