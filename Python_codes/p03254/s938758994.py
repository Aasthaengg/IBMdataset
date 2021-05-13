n,x=map(int,input().split())
List=list(map(int,input().split()))
List.sort()
ans=0
if sum(List)==x:
    print(n)
    exit()
else:
    for i in range(len(List)-1):
        if x>=List[i]:
            ans+=1
            x-=List[i]
        else:
            break
print(ans)