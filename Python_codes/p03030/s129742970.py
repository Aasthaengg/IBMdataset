n=int(input())
l=[]
for i in range(n):
    temps,tempp=input().split()
    temp=[temps,int(tempp),i+1]
    l.append(temp)

l.sort(key=lambda x:x[1],reverse=True)
l.sort(key=lambda x:x[0])
for i in range(n):
    print(l[i][2])
