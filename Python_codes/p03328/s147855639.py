a,b=map(int,input().split())

res=1
A=[res]
for i in range(2,1000):
    res+=i
    A.append(res)
    if A[i-2]-a==res-b:
        print(res-b)
        exit()
