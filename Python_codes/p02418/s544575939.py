import re
s=input()
p=input()
s_s=s+s
match=re.search(p,s_s)
if match:
    print('Yes')
else:
    print('No')
