a = input()
n = len(a)
r = 0
g ,p =0, 0
for i in a:
    if i =="g":
        if g>p:
            r+=1
            p+=1
        else:
            g+=1
    else:
        if g>p:
            p+=1
        else:
            g+=1
            r-=1
print(r)
