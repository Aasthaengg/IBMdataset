n,m=map(int,input().split())

# p:県　y:誕生年
py=[]

# [p y number]
for i in range(m):
    py.append(list(map(int,input().split())))
    py[i].append(i)
py=sorted(py,key= lambda x:(x[0],x[1]))

for i in range(m):
    if i==0:
        py[i][1]=1
    else:
        if py[i][0]==py[i-1][0]:
            py[i][1]=py[i-1][1]+1
        else:
            py[i][1]=1
py=sorted(py,key=lambda x:(x[2]))

for i in range(m):
    temp1="0"*(6-len(str(py[i][0])))+str(py[i][0])
    temp2="0"*(6-len(str(py[i][1])))+str(py[i][1])
    print(temp1+temp2)

