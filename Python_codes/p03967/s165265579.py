s=input()
g,p=0,0
w,l=0,0
for c in s:
    if g>p:
        p+=1
        if c=='g':
            w+=1
    else:
        g+=1
        if c=='p':
            l+=1
print(w-l)