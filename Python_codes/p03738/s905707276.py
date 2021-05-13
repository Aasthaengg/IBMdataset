a=str(input())
s=len(a)
b=str(input())
t=len(b)
if s>t:
    print('GREATER')
elif s<t:
    print('LESS')
else:
    for i in range(s):
        if a[i]>b[i]:
            print('GREATER')
            break
        elif a[i]<b[i]:
            print('LESS')
            break
    else:
        print('EQUAL')