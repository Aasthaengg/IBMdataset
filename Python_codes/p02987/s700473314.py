# coding: utf-8
s = input()
ss = sorted(s)
if (ss[0] == ss[1] and ss[2] == ss[3] and ss[1] != ss[2]):
    print("Yes")
else:
    print("No")
