n=int(input())
lr=[list(map(int,input().split())) for _ in range(n)]
k=[]
for i in range(n):
    k.append(lr[i][1]-lr[i][0]+1)
print(sum(k))