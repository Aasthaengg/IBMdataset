power=[1,2]

if __name__ == '__main__':
    N,M=list(map(int,input().split()))
    data=[list(map(int,input().split())) for i in range(N)]
    ans=0
    for i in power:
        for j in power:
            for k in power:
                temp=[]
                for cake in data:
                    temp.append(cake[0]*(-1)**i+cake[1]*(-1)**j+cake[2]*(-1)**k)
                temp.sort()
                temp2=temp[-M:]
                ans=max(ans,sum(temp2))

    if M==0:
        print(0)
    else:
        print(ans)


