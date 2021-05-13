import sys
s=input()
k=int(input())
for i in range(len(s)):
    if s[i]!="1":
        print(s[i])
        sys.exit()
    if s[i]=="1" and i+1==k:
        print(1)
        sys.exit()
