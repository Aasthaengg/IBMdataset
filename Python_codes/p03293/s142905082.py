s = input()
t = input()
import sys
if s==t:
    print("Yes")
    sys.exit()
for i in range(1,len(s)):
    if s[-i:]+s[:-i]==t:
        print("Yes")
        sys.exit()
else:
    print("No")