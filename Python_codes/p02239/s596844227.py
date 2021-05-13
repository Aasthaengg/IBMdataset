n=int(input())

lst=[0]*n

for _ in range(n):
    work=list(map(int,input().split()))
    lst[work[0]-1]=work[2:]

dis=[-1]*n
dis[0]=0
work=lst[0][:]
work_next=[]
token=0

while work:
    token+=1
    for x in work:
        if dis[x-1]==-1: dis[x-1]=token
        for y in lst[x-1]:
            if dis[y-1]==-1 : work_next.append(y)
    work=work_next[:]
    work_next=[]

for i in range(n):
    print("{} {}".format(i+1,dis[i]))
