n=int(input())

k=2
while(2*n > k*(k-1)):
    k+=1

if(2*n!=k*(k-1)):
    print("No")
else:
    print("Yes")
    print(k)
    tmp=0
    result=[[0]*(k-1) for i in range(k)]
    for i in range(k):
        for j in range(i):
            result[i][j]=result[j][i-1]
        for l in range(k-i-1):
            tmp+=1
            result[i][i+l]=tmp
        
    for j in range(k):
        print("{} ".format(k-1),end="")
        for i in range(k-2):
            print("{} ".format(result[j][i]),end="")
        print(result[j][k-2])