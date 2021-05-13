from collections import Counter

s=Counter(input())
b,m=max(s.values()),min(s.values())
kind = len(s.keys())
if kind==3:
    if b-m<=1: print("YES")
    else: print("NO")
elif kind==2:
    if b==1 and m==1: print("YES")
    else: print("NO")
else:
    if b==1: print("YES")
    else: print("NO")