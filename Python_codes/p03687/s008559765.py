s=input()
l=[chr(i) for i in range(ord("a"),ord("z")+1)]
a=100
for i in l:
    t=0
    c=0
    for j in s:
        if j!=i:
            c+=1
        else:
            if t<c:
                t=c
            c=0
    t=max(t,c)
    if a>t:
        a=t
print(a)