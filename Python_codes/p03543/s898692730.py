import math

s=input()
n=len(s)
flag=False
if s[0]==s[1]==s[2]:
    flag=True
if s[1]==s[2]==s[3]:
    flag=True
if flag==True:
    print("Yes")
else:
    print("No")