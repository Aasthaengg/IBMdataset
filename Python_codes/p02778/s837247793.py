import re

N = input()
N = re.sub(r'[A-z]', 'x', N)

print(N)