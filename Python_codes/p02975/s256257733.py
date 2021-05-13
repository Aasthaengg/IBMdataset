import collections
n = int(input())
a = list(map(int,input().split()))
c = collections.Counter(a)

if len(c) > 3:
    print("No")
    exit()
elif len(c) == 3:
    if n % 3 != 0:
        print("No")
        exit()
    p = []
    for k , v in c.items():
        if v != n//3:
            print("No")
            exit()
        p.append(k)
    if (p[0] ^ p[1]) ^ p[2] != 0:
        print("No")
        exit()
elif len(c) == 2:
    if n % 3 != 0:
        print("No")
        exit()
    for k,v in c.items():
        if k == 0:
            if v != n//3:
                print("No")
                exit()
        else:
            if v != 2*n//3:
                print("No")
                exit()
elif len(c) == 1:
    for k in c.keys():
        if k != 0:
            print("No")
            exit()
            
print("Yes")