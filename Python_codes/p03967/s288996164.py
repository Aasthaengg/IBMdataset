s=input()
g=0
p=0
point=0
for i in range(len(s)):
    o=s[i]
    if o=="g":
        if p+1<=g:
            point+=1
            p+=1
        else:
            g+=1
    else:
        if p+1<=g:
            p+=1
        else:
            point-=1
            g+=1
print(point)