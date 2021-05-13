s=input()
a=len(s)
for i in set(s):
    ss=s
    j=0
    while len(set(ss))>1:
        t=""
        for k in range(len(ss)-1):
            if i in (ss[k],ss[k+1]):
                t+=i
            else:
                t+=ss[k]
        ss=t
        j+=1
    a=min(a,j)
print(a)