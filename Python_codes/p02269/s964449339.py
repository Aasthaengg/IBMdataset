d={}
for _ in range(int(input())):
    a,b=input().split()
    if a=='find':
        if b in d:print('yes')
        else:print('no')
    else:d[b]=0