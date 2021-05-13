import sys
n=int(input())
t=[]
for i in range(n):
    t.append(list(map(int,input().split())))
for i,d in enumerate(t):
    if i>0:
        b=d[0]-a
        c=abs(d[1]+d[2]-aa)
    a=d[0]
    aa=d[1]+d[2]
    if i==0:
        if not (a >= aa and a % 2 == aa % 2):
            print('No')
            sys.exit()
        else:
            continue
    if not (b>=c and b%2==c%2):
        print('No')
        sys.exit()
print('Yes')