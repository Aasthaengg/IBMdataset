import sys
s = list(input())
t = list(input())
ss = "".join(s)
tt = "".join(t)
ls = []
for i in range(len(ss)-len(tt)+1):
    l = s[i:i+len(tt)]
    for j in range(len(tt)):
        if l[j] != t[j] and l[j] != "?":
            break
        else:
            l[j] = t[j]
    else:
        l = "".join(l)
        l = "".join(s[:i]) + l + "".join(s[i+len(tt):])
        l = l.replace("?","a")
        ls.append(l)
if ls == []:
    print("UNRESTORABLE")
else:
    ls.sort()
    print(ls[0])
            
    
            
