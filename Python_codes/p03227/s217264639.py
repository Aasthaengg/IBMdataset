# coding: utf-8
 
s = input().strip()
if len(s) == 2:
    print(s)
else:
    ans = s[::-1]
    print(ans)