import sys
import math
import itertools
#n=int(input())
def isLoop(s):
    if (s[0] == s[-1] and s[1] == s[-2]):
        return True
    else:
        return False
a, b = map(int, input().split())
ans=0
for i in range(a, b + 1):
    if (isLoop(str(i))):
        ans += 1
print(ans)