import sys
s=input()
for i in range(len(s)):
    if i%2==0 and "L" in s[i]:
        print("No")
        sys.exit()
    elif i%2==1 and "R" in s[i]:
        print("No")
        sys.exit()
print("Yes")