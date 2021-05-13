from collections import deque
s=input()
d=[]

for i in s:
    if i=="S":
        d.append("S")
    elif i=="T" and (not d or d[-1]=="T"):
        d.append("T")
    else:
        d.pop()
print(len(d))
    
