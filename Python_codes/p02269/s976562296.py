n=int(input())
D=set()
for i in range(n):
    command,str_=input().split()
    if command=='insert':
        D.add(str_)
    elif command=='find':
        if str_ in D:
            print('yes')
        else:
            print('no')
