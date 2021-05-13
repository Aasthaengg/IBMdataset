#B
import sys
s = list(input())
one=["R", "U", "D"]
two=["L", "U", "D"]
for i in range(len(s)):
    if i % 2 == 0 and (one[0] != s[i] and one[1]!=s[i] and one[2]!=s[i]):
        print("No")
        sys.exit()
    if i % 2 != 0 and(two[0] != s[i] and two[1]!=s[i] and two[2]!=s[i]):
        print("No")
        sys.exit()
print('Yes')