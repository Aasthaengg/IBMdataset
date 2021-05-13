W,a,b = map(int,input().split())

if a<b:
    l = a
    r = b
else:
    l = b
    r = a

if W+l>=r:
    print(0)
else:
    print(r-(W+l))