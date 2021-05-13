N=int(input())
lis=[]
for i in range(1,N+1):
    for j in range(N):
        if i%(2**j)==0:
            lis.append(j)
print(2**max(lis))