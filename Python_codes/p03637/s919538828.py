n=int(input())

t = list(map(int,input().split()))

yonba = 0
gusu = 0
kisu = 0

for i in t:
    if i%4==0:
        yonba += 1
    elif i%2==0:
        gusu += 1
    else:
        kisu += 1

if kisu==0:
    print('Yes')
else:
    if kisu <= yonba:
        print('Yes')
    else:
        if kisu-yonba==1 and gusu == 0:
            print('Yes')
        else:
            print('No')