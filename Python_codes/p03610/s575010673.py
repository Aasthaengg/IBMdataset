import sys
import math
s = input()
ans=''
if (len(s) % 2 == 0):
    for i in range(0, len(s), 2):
        ans+=s[i]
else:
    for i in range(0, len(s)+1, 2):
        ans += s[i]
print(ans)