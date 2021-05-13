import re

S = input()

p = re.compile("^(A)?(KIH)(A)?(B)(A)?(R)(A)?$")

if(p.match(S)):
    print('YES')
else:
    print('NO')