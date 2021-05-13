S=list(input())
a=S.count('0')
b=S.count('1')
if a>b:
    print(2*b)
else:
    print(2*a)