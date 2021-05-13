s=input()
t=input()
if len(s)==len(t):
    cm=0
    for i in range(len(s)):
        if s[i]!=t[i]:
            cm+=1
else:
    cm=1000
    for i in range(len(s)-len(t)):
        cn=0
        for j in range(len(t)):
            if s[i+j]!=t[j]:
                cn+=1
        cm=min(cm,cn)

print(cm)
