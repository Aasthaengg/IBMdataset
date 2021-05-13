N=int(input())
c=[[0]*10 for i in range(10)]
for n in range(1,N+1):
    c[int(str(n)[0])][int(str(n)[-1])]+=1
sum=0
for i in range(10):
    for j in range(10):
        sum+=c[i][j]*c[j][i]
print(sum)
