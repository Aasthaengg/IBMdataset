n = int(input())
ls = list(map(int,input().split()))
di = [0]*(n+1)
ls = [0] + ls + [0]
for i in range(n+1):
    di[i] = abs(ls[i+1] - ls[i])
mx = sum(di)
for j in range(1,n+1):
    print(mx-di[j-1]-di[j]+abs(ls[j+1]-ls[j-1]))