H,W=map(int,input().split())
N=int(input())
a=list(map(int,input().split()))

c=[[0 for j in range(W)] for i in range(H)] # 0-initial
cnt=0
for i,ai in enumerate(a):
    for t in range(ai):
        c[cnt//W][cnt%W]=i+1
        cnt+=1
for i in range(H):
    if i%2==1:
        c[i].reverse()

for ci in c:
    print(*ci)