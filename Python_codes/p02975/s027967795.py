from collections import Counter
n = int(input())
a = list(map(int,input().split()))
if a.count(0) == n:
    print("Yes")
    exit()

if n%3 != 0:
    print("No")
    exit()

c = Counter(a)
if len(c) == 2:
    if 0 not in c.keys():
        print("No")
        exit()
    if c[0] != n//3:
        print("No")
    else:
        print("Yes")
elif len(c) == 3:
    x = 0
    for i,j in c.items():
        if j != n//3:
            print("No")
            exit()
        x ^= i
    if x:
        print("No")
    else:
        print("Yes")

else:
    print("No")
