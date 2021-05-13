L,R = map(int,input().split())
r = 2019
if R//2019 != L//2019:
    print(0)
else:
    Rmod = R%2019
    Lmod = L%2019
    for i in range(Lmod,Rmod+1):
        for j in range(i+1,Rmod+1):
            r = min(r,(i*j)%2019)
    print(r)
