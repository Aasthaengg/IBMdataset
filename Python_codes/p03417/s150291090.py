a,b = map(int, open(0).read().split())

if a==1 and b==1:
    print(1)
elif 1 in [a,b]:
    x = a*b
    print(x-2)
else:
    print((a-2)*(b-2))