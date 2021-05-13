from collections import deque

N,M=map(int,input().split())
graph=[[] for i in range(N+1)]
for i in range(M):
    A,B=map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)
dist=[-1]*(N+1)
dist[0]=0
dist[1]=0
d=deque()
d.append(1)
ans=[0]*(N+1)
while d:
    v=d.popleft()
    for i in graph[v]:
        if dist[i]!=-1:
            continue
        dist[i]=dist[v]+1
        d.append(i)
        if ans[i]!=0:
            continue
        ans[i]+=v
print("Yes")
for i in ans:
    if i==0:
        continue
    print(i)     



    









        

    









    

        




    















    



    





    






        






    
















        


























            
    


    


    
    














    


    












