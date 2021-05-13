N=int(input())
plus=[]
other=[]
d=list(map(int,input().split()))
for num in d:
    if num>0:
        plus.append(num)
    else:
        other.append(num)
if len(plus)>0:
    K=len(plus)
    if K==1:
        data=[]
        ans=plus[0]
        for q in other:
            data.append((ans,q))
            ans+=abs(q)
        print(ans)
        for some in data:
            x,y=some
            print(x,y)

    else:
        data=[]
        if len(other)>=1:
            ans=other[-1]
            for some in plus[1:]:
                data.append((ans,some))
                ans-=some
            other[-1]=ans
            ans=plus[0]
            for q in other:
                data.append((ans,q))
                ans+=abs(q)
            print(ans)
            for some in data:
                x,y=some
                print(x,y)
        else:
            plus.sort()
            ans=plus[0]
            for some in plus[1:-1]:
                data.append((ans,some))
                ans-=some
            data.append((plus[-1],ans))
            ans=plus[-1]-ans
            print(ans)
            for some in data:
                x,y=some
                print(x,y)
            
elif len(plus)==0:
    other.sort(reverse=True)
    data=[]
    ans=other[0]
    for q in other[1:]:
        data.append((ans,q))
        ans+=abs(q)
    print(ans)
    for some in data:
        x,y=some
        print(x,y)
