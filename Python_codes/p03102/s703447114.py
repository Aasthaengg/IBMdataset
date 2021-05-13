n,m,c=map(int,input().split())
b=list(map(int, input().split()))
res = 0
for i in range(n):
    a=list(map(int, input().split()))
    sum = 0
    for j in range(m):
        sum += a[j]*b[j]
    if sum+c > 0:
        res +=1
print(res)