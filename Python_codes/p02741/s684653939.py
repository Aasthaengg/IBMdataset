k=int(input())
two={4,6,9,10,14,21,22,25,26}
f={8,12,18,20,27}
if k in two:
    print(2)
elif k in f:
    print(5)
elif k==16:
    print(14)
elif k==24:
    print(15)
elif k==28 or k==30:
    print(4)
elif k==32:
    print(51)
else:
    print(1)
