n=int(input())
t=list(map(int, input().split()))
sum=sum(t)
m=int(input())
p=[list(map(int, input().split())) for _ in range(m)]
for i in range(m):
    n=p[i][0]-1
    print(sum-t[n]+p[i][1])