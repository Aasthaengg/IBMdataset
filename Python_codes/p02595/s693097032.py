#B
n,d=map(int,input().split())
xy=[list(map(int,input().split()))for _ in range(n)]
count=0
for i in xy:
    if pow(i[0],2)+pow(i[1],2)<=pow(d,2):
        count+=1
print(count)
