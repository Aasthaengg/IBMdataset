X,Y=[int(x) for x in input().rstrip().split()]
ans=[]
cnt=1
now=X
for i in range(1,Y+1):
    now=now*2
    if now<=Y:
        cnt+=1

    else:
        break
print(cnt)