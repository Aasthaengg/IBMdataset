import sys

a,b,c = map(int,input().split())

val = [a,b,c]

for i in val:
    if 1 >= i and i <= 100:
        print('No')
        sys.exit()

if val[0] == val[1] and val[1] == val[2]:
    print('Yes')
else:
    print('No')