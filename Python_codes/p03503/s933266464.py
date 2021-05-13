n=int(input())
f=[list(map(int,input().split())) for _ in range(n)]
p=[list(map(int,input().split())) for _ in range(n)]
x=[]
for i in range(1,2**10):
    j_open=format(i,'b').zfill(10)
    pro_sum=0
    for j in range(n):
        one_sum=0
        for k in range(10):
            if f[j][k]==1 and j_open[k]=='1':one_sum+=1
        pro_sum+=p[j][one_sum]
    x.append(pro_sum)
print(max(x))