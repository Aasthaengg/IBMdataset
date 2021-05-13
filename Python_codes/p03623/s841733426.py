x,a,b=[int(i) for i in input().split()]

alen=abs(x-a)
blen=abs(x-b)

if alen<blen:
    print("A")
else:
    print("B")