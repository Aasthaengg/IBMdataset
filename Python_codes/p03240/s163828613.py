n=int(input())
lst=[None]*n
for i in range(n):
    a,b,c=map(int,input().split())
    lst[i]=[a,b,c]
lst=sorted(lst,key=lambda x:x[2],reverse=True)
for i in range(101):
    for j in range(101):
        switch=0
        x,y,z=lst[0]
        height=z+abs(i-x)+abs(j-y)
        for k in range(1,n):
            x,y,z=lst[k]
            if z==0:
                if abs(i-x)+abs(j-y)<height:
                    switch=1
                    break
            elif abs(i-x)+abs(j-y)+z!=height:
                switch=1
                break
        if switch==0:
            print(i,j,height)