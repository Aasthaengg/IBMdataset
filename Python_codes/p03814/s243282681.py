import sys
import re
s = str(input())
if len(s) < 0 or len(s) > 200000:
    sys.exit()

array_str = re.findall(r'A.*Z', s)
max = 0
for I in array_str:
    if len(I) > max:
        max = len(I)
print(max)
