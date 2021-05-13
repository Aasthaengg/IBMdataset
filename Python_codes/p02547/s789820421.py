n = int(input())

p=0
for i in range(n):
    x,y=map(int,input().split())
    if x==y:
        p+=1
        if p==3:
            print('Yes')
            exit()
    else:
        p=0
else:
    print('No')