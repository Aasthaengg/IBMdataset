import itertools

n=int(input())

f=[list(map(int,input().split())) for i in range(n)]#operation

p=[list(map(int,input().split())) for i in range(n)]#inference

lis=[]
for i in list(itertools.product([0,1],repeat=10))[1:]:
    lisi=0
    for j in range(n):
        sj=0
        for k in range(10):
            sj+=i[k]*f[j][k]
        lisi+=p[j][sj]
    lis.append(lisi)

print(max(lis))