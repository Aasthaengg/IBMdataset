#Crossing
n=int(input())
flag=False
index=0
for i in range(1000):
    if i*(i+1)//2==n:
        flag=True
        index=i
        break
if flag:
    print("Yes")
    print(i+1)
    uselist=[[1],[1]]
    if index==1:
        print(1,1)
        print(1,1)
    else:
        def plus(N):
            base=(N)*(N-1)//2
            for k in range(1,N+1):
                uselist[k-1].append(base+k)
            uselist.append([base+i+1 for i in range(N)])

     
        
        for k in range(2,index+1):
            plus(k)
        for some in uselist:
            print(index,*some)
            
else:
    print("No")