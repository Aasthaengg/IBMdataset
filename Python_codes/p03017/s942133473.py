n,a,b,c,d=map(int,input().split())
s=input()

if c<d:
    for i in range(b,d):
        if s[i:i+2]=='##':
            print('No')
            exit()
    for i in range(a,c):
        if s[i:i+2]=='##':
            print('No')
            exit()
    print('Yes')
else:
    for i in range(b,d):
        if s[i:i+2]=='##':
            print('No')
            exit()
    for i in range(a,c):
        if s[i:i+2]=='##':
            print('No')
            exit()
    for i in range(b-2,d-1):
        if s[i:i+3]=='...':
            print('Yes')
            exit()
    print('No')
