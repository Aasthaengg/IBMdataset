x=list(map(int,input().split()))
x.sort()
if (x[0]==x[1])or(x[1]==x[2]):
    if x[0] == x[1] == x[2]:
        print(1)
    else:
        print(2)
else:
    print(3)