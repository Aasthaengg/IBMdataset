N=int(input())
lr=[list(map(int,input().split())) for i in range(N)]
count=0
for i in range(N):
    count=count+lr[i][1]-lr[i][0]+1
print(count)