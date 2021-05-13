N,M,X=map(int,input().split())
A=[list(map(int,input().split())) for i in range(N)]
ans=[]
for i in range(2**N):
    cost=0
    m=[0]*M
    for j in range(N):
        if ((i>>j)&1):
            cost+=A[j][0]
            for k in range(M):
                m[k]+=A[j][k+1]
    m7=[l for l in m if X<=l]
    if len(m7)==M:
        ans.append(cost)
if len(ans)>0:
    print(min(ans))
else:
    print(-1)

        




    















    



    





    






        






    
















        


























            
    


    


    
    














    


    












