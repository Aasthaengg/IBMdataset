n,a,b,c=map(int,input().split())
l=[int(input()) for _ in range(n)]
ABC=(a,b,c)

import itertools
kouho=list(itertools.product(range(4), repeat=n))
ans=10**9
for item in kouho:

    if 0 in item and 1 in item and 2 in item:
        cost=0
        abc=[0]*3

        for i,v in enumerate(item):
            if v<3:
                if abc[v]>0:
                    cost+=10
                abc[v]+=l[i]

        for i in range(3):
            cost+=abs(abc[i]-ABC[i])
        #print(item,cost)
        ans=min(ans,cost)

print(ans)


    
    












        
