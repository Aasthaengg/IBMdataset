
import re

s = input()
pattern = re.compile("(A?KIHA?BA?RA?)")

ret = pattern.findall(s)

ret2 = pattern.findall("[^AKIHBR]")


#print(ret)
if ret is not None and len(ret) ==  1 and len(ret[0]) == len(s):
    ans = "YES"
else:
    ans = "NO"

print(ans)