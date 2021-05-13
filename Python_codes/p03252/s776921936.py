
s=list(input())
t=list(input())
l=len(s)

henkan1 = {chr(ord("a")+i) : set() for i in range(26) }
henkan2 = {chr(ord("a")+i) : set() for i in range(26) }

for i in range(l):
#    if s[i]!=t[i]:
    henkan1[s[i]].add(t[i])
    henkan2[t[i]].add(s[i])
        
if all(len(h) <=1 for h in henkan1.values()) and all(len(h) <=1 for h in henkan2.values()):
    print("Yes")
else:
    print("No")