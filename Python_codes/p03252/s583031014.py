s=input()
t=input()
n=len(s)
d={}
for i in range(n):
    ss=s[i]
    tt=t[i]
    if ss in d and (ss,tt) not in d.items():
        print("No")
        exit()
    if tt in d.values() and (ss,tt) not in d.items():
        print("No")
        exit()
    if ss not in d:
        d[ss]=tt    
print("Yes")