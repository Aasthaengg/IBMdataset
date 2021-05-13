n,k=map(int,input().split())
l=[[*map(int,input().split())] for i in range(n)]
l.sort(key=lambda x:x[0])
for i,j in l:
    k-=j
    if k<=0:
        print(i)
        break