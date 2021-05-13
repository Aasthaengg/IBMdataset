import itertools
a=[]
for i in range(5):
    a.append(int(input()))
out=sum(a)+50
ls = list(itertools.permutations(range(5)))
for i in ls:
    t=0
    for j in i:
        if t%10 != 0:
            t+=10-t%10
        t+=a[j]
    if t <=out:
        out=t
print(out)