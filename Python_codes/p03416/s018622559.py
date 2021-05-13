A,B=map(int,input().split())
k=0
for i in range(A,B+1):
    if i//10000-i%10==0:
        j=i%10000//10
        if j//100-j%10==0:
            k=k+1


            
print(k)            