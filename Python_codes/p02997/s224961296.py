N,K=map(int,input().split())

limit=(N*(N-1)//2)-(N-1)
Ans=[]
#N-1本引く
for index in range(2,N+1):
    Ans.append((1,index))

if K>limit:
    print('-1')
else:
    rest=limit-K
    From=2
    To=3

    while rest:
        Ans.append((From,To))
        To+=1
        if To==N+1:
            From+=1
            To=From+1
        rest-=1
    
    print(len(Ans))
    for i in range(len(Ans)):
        print('{0} {1}'.format(Ans[i][0],Ans[i][1]))
        

