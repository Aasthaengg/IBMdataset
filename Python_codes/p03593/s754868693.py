from collections import Counter
h,w = map(int,input().split())
A = [input() for _ in range(h)]
s = []
for a in A:
    for c in a:
        s.append(c)
c = Counter(s)
if h==1 and w==1:
    print('Yes')
else:
    x,y,z = 0,0,0
    for v in c.values():
        if v%4==0:
            x += 1
        elif v%4==2:
            y += 1
        else:
            z += 1
    if h%2==0 and w%2==0:
        print('Yes' if (y==0 and z==0) else 'No')
    elif h%2==0 or w%2==0:
        if z!=0:
            print('No')
        else:
            if h%2==0 and y<=h//2:
                print('Yes')
            elif w%2==0 and y<=w//2:
                print('Yes')
            else:
                print('No')
    else:
        if z!=1:
            print('No')
        else:
            if y<=(h-1)//2 + (w-1)//2:
                print('Yes')
            else:
                print('No')