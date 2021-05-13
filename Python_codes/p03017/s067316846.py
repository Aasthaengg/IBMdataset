import sys
n, a, b, c, d = map(int, input().split())
s = input()
if any(s[i]==s[i+1]=="#" for i in range(a-1, c-2)) or any(s[i]==s[i+1]=="#" for i in range(b-1, d-2)):
    print("No")
elif c<d:
    print("Yes")
else:
    for i in range(b-1, d):
        if s[i-1]==s[i]==s[i+1]==".":
            print("Yes")
            sys.exit()
    print("No")
