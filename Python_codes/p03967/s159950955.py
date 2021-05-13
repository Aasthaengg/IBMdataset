S=input()
p=0
g=0
for s in S:
    if s=="g":
        g+=1
    else:
        p+=1
print((g-p)//2)