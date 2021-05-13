N=str(input())
cc=['+']*3
ans=int(N[0])
for j in range(2**3):
    temp=bin(2**3+j)
    for i in range(3,6):
        if temp[i]=='0':
            ans+=int(N[i-2])
            cc[i-3]='+'
        else:
            ans-=int(N[i-2])
            cc[i-3]='-'
    if ans==7:
        print(N[0]+cc[0]+N[1]+cc[1]+N[2]+cc[2]+N[3]+'=7')
        exit()
    else:
        ans=int(N[0])