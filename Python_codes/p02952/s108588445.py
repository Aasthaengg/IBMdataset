N=int(input())
count=0
for i in range(1,N+1):
    for j in range(0,6):
        if 10**j <=i <10**(j+1):
            ans=j+1
            if (j+1)%2!=0:
                count+=1
                
print(count)      