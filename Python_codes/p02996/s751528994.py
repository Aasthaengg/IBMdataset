n=int(input())
l=[]
for i in range(n):
    a,b=map(int,input().split())
    l.append((a,b))
l.sort(key=lambda x:x[1])
tmp=0
for i in range(n):
    tmp+=l[i][0]
    if tmp>l[i][1]:
        print("No")
        exit()
print("Yes")