l = list(map(int,input().split()))

l.sort()

if  l[0] != l[1]:
    print((l[1] * 2 ) - 1)

elif l[0] == l[1]:
    print(l[1] * 2)
