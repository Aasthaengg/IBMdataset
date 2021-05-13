N=int(input())
lis = [[0 for i in range(10)] for i in range(10)]
for i in range(1,N+1):
    fir = i//(10**(len(str(i))-1))
    las = i%10
    lis[fir][las]+=1
sum=0
for i in range(0,10):
    for j in range(i,10):
        if i==j:
            sum+=lis[i][j]*(lis[i][j]-1)+lis[i][j]
        else:
            sum+=lis[i][j]*lis[j][i]*2

#print(*lis, sep="\n")
print(sum)
