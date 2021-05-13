l=map(complex,[0,1e2])
for _ in range(input()):
    t,l=l,[0]
    for i,j in zip(t[:-1],t[1:]):
        d=(j-i)/3
        l.extend((i+d,i+d+d*complex(1,3**0.5)/2,i+d*2,j))
for i in l:
    print i.real,i.imag