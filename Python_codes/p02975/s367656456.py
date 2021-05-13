from collections import Counter
n = int(input())
a = list(map(int,input().split()))
c = Counter(a)
if len(c) == 3:
    l = list(c.keys())
    v = list(c.values())
    if l[0]^l[1]^l[2] == 0 and v[0]==v[1]==v[2]:
        print("Yes")
    else:
        print("No")
elif len(c) == 1:
    if list(c.keys())[0] == 0:
        print("Yes")
    else:
        print("No")
elif len(c) == 2:
    if (0 not in a):
        print("No")
    else:
        v = c[0]
        if len(a) == c[0]*3:
            print("Yes")
        else:
            print("No")
else:
    print("No")