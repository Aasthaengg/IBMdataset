n,x,y=map(int, input().split())
cnts=[0]*n
for i in range(1,n+1):
    for j in range(1,i):
        mn=min(abs(i-j),abs(i-x)+abs(j-y)+1,abs(i-y)+abs(j-x)+1)
        cnts[mn]+=1
for ci in cnts[1:]:
    print(ci)
