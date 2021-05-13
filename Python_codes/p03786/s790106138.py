n,*a=map(int,open(0).read().split())
a.sort()
b=[0]
for i in a:
    b+=[i+b[-1]]
for i in range(n+1)[::-1]:
    if b[i]/3>b[i-1]:
        print(n-i+1)
        break