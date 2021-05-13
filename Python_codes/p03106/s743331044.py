import sys
a,b,k = map(int,input().split())
c = 0
if a > b:    
    for i in range(b,0,-1):
        if (b%i == 0) and (a%i == 0):
            c += 1
            if c == k:
                print(i)
                sys.exit()
else:
    for i in range(a,0,-1):
        if (b%i == 0) and (a%i == 0):
            c += 1
            if c == k:
                print(i)
                sys.exit()