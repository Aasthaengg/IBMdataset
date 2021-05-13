w,a,b = map(int,input().split())
aw = w+a
bw = w+b

if a > b:
    if bw >= a:
        print(0)
    else:
        print(a-bw)
else:
    if aw >= b:
        print(0)
    else:
        print(b-aw)