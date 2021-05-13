n,c,k=map(int,input().split())

cnt=0


time=[]
for _ in range(n):
    time.append(int(input()))


time.sort()

count_up=0
member=0
cnt=0

temp=[]

for t in time:
    if count_up==0:
        count_up=t

    if t>count_up+k:
        #print(temp)
        cnt+=1
        count_up=t
        member=1
        temp=[t]
    else:
        member+=1
        temp.append(t)
        if member>=c:
            #print(temp)
            member=0
            cnt+=1
            count_up=0
            temp=[]

if member>0:
    cnt+=1
    #print(temp)

print(cnt)
    




