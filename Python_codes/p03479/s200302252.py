X,Y=map(int,input().split())
atmp=X
ans=1
for _ in range(65):
    if atmp*2<=Y:
        ans+=1
        atmp*=2
    else:
        print(ans)
        break
