n=int(input())
F=[None for i in range(n+1)]
F[0],F[1]=1,1
for i in range(2,n+1):
    F[i]=F[i-2]+F[i-1]

answer=F[n]
print(answer)
