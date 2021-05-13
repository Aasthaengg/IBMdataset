def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1
def has_duplicates(seq):
    return len(seq) != len(set(seq))
s=int(input())
a=list()
a.append(s)
i=0
while True:
    a.append(f(a[i]))
    double=has_duplicates(a)
    if double==True:
        print(i+2)
        break
    i+=1