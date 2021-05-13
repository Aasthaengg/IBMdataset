import sys
x=int(input())

for j in range(1,361):
    for k in range(1,361):
        if 360*k==x*j:
            print(j)
            sys.exit()