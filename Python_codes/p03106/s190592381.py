A,B,K=map(int,input().split())

mamax=max(A,B)
count=0
for i in range(mamax,0,-1):
    if(A%i==0 and B%i==0):

        count=count+1
        if(count==K):
            print(i)
            exit()
