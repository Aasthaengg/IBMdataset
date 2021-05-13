N,X=map(int,input().split())
m=[int(input()) for i in range(N)]
m.sort()
sum=0
for i in range(N):
    sum+=m[i]
print((X-sum)//m[0]+N)
