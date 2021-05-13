import sys
n = int(input())
a = list(map(int, input().split()))
b = 0
while True:
    c = 0
    for i in a:
        a[c]=i//2
        c+=1
        if i%2 != 0:
            print(b//n)
            sys.exit(0)
        b+=1
