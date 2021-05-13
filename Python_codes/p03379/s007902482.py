n=int(input())
#a,b=map(int,input().split())
xl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
l2d=[]
for i in range(n):
    l2d.append([i,xl[i]])

xlsort=sorted(xl)
v1=xlsort[n//2-1]
v2=xlsort[n//2]

l2d.sort(key=lambda x: x[1])
dic={}
for i in range(n):
    dic[l2d[i][0]]=i
thre=n//2
for i in range(n):
    if dic[i]<thre:
        print(v2)
    else:
        print(v1)

