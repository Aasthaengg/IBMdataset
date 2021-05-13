import collections

_=input()
a=list(map(int,input().split()))
c=collections.Counter(a)
l=sorted(c.items(), key=lambda x: x[0])
x=0
for i in l[::-1]:
    if i[1]>3:
        if x:
            print(i[0]*x)
            exit(0)
        else:
            print(i[0]*i[0])
            exit(0)
    elif i[1]>1:
        if x:
            print(i[0]*x)
            exit(0)
        else:
            x=i[0]
print(0)