#15
import sys

s = input()
l = len(s) 
for i in range(l+1):
    for j in range(l+1):
        mozi1 = s[0:i]
        mozi2 = s[j:]
        if mozi1+mozi2 == "keyence":
            print("YES")
            sys.exit()
print("NO")