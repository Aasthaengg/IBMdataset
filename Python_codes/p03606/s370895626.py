n=int(input())
lr=[list(map(int,input().split())) for a in range(n)]
sum=0
for v in lr:
    sum+=v[1]-v[0]
print(sum+n)