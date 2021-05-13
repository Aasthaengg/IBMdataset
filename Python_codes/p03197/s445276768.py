n,*a=map(int,open(0).read().split())

for aa in a:
    if aa%2==1:
        print('first')
        exit(0)

print('second')