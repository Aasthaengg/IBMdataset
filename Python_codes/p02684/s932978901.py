N,K=map(int,input().split())
A=list(map(int,input().split()))
l=[1]
X=[True]*N
X[0]=False
num=1
for i in range(K):
    num=A[num-1]
    if X[num-1]:
        l.append(num)
        X[num-1]=False
    else:
        q=l.index(num)
        l=l[q:]
        print(l[(K-q)%len(l)])
        exit()
print(l[-1])

    

        




    















    



    





    






        






    
















        


























            
    


    


    
    














    


    












