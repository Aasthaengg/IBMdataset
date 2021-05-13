n,k=map(int,input().split())
c=0
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
l.sort()
for i in range(n):
    c+=l[i][1]
    if(c>=k):
        print(l[i][0])
        exit()
