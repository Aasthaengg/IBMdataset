n,m=map(int,input().split())
num=[]
ans=[""]*m
numcount=[1]*n
count=1
for i in range(m):
    p,y=map(int,input().split())
    num.append([p,y,i])
stry= lambda val: val[1]
num.sort(key=stry)
for i in range(m):
    p=str(num[i][0])
    y=str(numcount[int(num[i][0])-1])
    numcount[int(num[i][0])-1]+=1
    ans[num[i][2]]="0"*(6-len(p))+p+"0"*(6-len(y))+y
for i in range(m):
    print(ans[i])
