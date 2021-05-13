n,*a=map(int,open(0).read().split())

b=sorted(a)
med=b[n//2]
medsmall=b[n//2-1]

for i in range(n):
    if med<=a[i]:
        print(medsmall)
    else:
        print(med)