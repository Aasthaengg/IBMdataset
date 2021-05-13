N=int(input())
d=[]
for _ in range(N):
    d.append(list(map(int,input().split())))
d.sort(key=lambda x:x[1])
sum_d=[0]*N
sum_d[0]=d[0][0]
for i in range(N-1):
    sum_d[i+1]=sum_d[i]+d[i+1][0]

for i in range(N):
    if sum_d[i]>d[i][1]:
        print('No')
        exit()
print('Yes')