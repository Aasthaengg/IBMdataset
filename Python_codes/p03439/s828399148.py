n=int(input())
i=0
j=n-1
print(i)
a=input()
print(j)
b=input()
while 1:
    if j-i<2:
        print(i)
        _=input()
        print(j)
        if input()!='Vacant':
            print('助けてくれ～～～')
    k=(j-i)//2+i
    print(k)
    c=input()
    if(k-i)%2and a==c or not(k-i)%2and a!=c:
        j=k
    else:
        a=c
        i=k