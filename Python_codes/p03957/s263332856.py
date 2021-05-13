s=input()
c=101
f=0
for i in range(len(s)):
    if s[i]=="C":
        c=min(c,i)
    elif s[i]=="F":
        f=max(f,i)

if s.count("C")>=1 and s.count("F")>=1 and f-c>0:
    print("Yes")
else:
    print("No")