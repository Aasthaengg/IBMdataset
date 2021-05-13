def prime(n):
    N=[1 for i in range(n+1)]
    N[0],N[1]=0,0
    for i in range(4,n+1,2):N[i]=0
    for i in range(3,int(n**0.5)+1):
        if N[i]==1:
            for j in range(i*2,n+1,i):
                N[j]=0
    return [i for i,j in enumerate(N) if j==1]


n=int(input())
num=prime(55555)
cnt,A=0,[]
for i in num:
    if i%5==1:
        A.append(i)
        cnt +=1
    if cnt==n:
        print(*A);exit()