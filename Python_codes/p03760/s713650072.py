o = str(input())
e = str(input())

if len(o) == len(e):
    for i in range(len(o)):
        print(o[i],end='')
        print(e[i],end='')

else:
    for i in range(len(o)-1):
        print(o[i],end='')
        print(e[i],end='')
    print(o[-1])
