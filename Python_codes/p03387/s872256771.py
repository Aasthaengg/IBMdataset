abc=sorted(list(map(int,input().split())))
abc[1]-=abc[0]
abc[2]-=abc[0]
abc[0]=0

if abc[1]%2==0:
    print(abc[2]-abc[1]//2)
else:
    print(abc[2]+1-(abc[1]-1)//2)
