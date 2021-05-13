import re
s=input()
p=input()
n=len(s)
pp='.*'.join(list(p))
print('Yes' if any([re.search(p,s[i:n]+s[0:i]) for i in range(0,n)]) else 'No')