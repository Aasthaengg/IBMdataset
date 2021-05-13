from collections import Counter
n=int(input())
a=list(map(int,input().split()))
c=Counter(a)
mod = 10**9 + 7
if n % 2 == 0:
    for i in a:
        if i % 2 == 0:
            print(0)
            exit()
    for i in c.values():
        if i != 2:
            print(0)
            exit()
    print(pow(2,n//2,mod))
if n % 2 == 1:
    for i in a:
        if i % 2 == 1:
            print(0)
            exit()
    if c[0]  == 1:
        c[0] = 2
    else:
        print(0)
        exit()
    for i in c.values():
        if i != 2:
            print(0)
            exit()
    print(pow(2,n//2,mod))
