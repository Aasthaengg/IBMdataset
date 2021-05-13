a=input()
b=input()
if len(a)>len(b):
    print('GREATER')
elif len(a)<len(b):
    print('LESS')
else:
    n=len(a)
    for i in range(n):
        if a[i]<b[i]:
            print('LESS')
            exit()
        if a[i]>b[i]:
            print('GREATER')
            exit()
    print('EQUAL')