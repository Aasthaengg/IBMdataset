n=int(input())
l=list()
for i in range(n):
    s,p=input().split()
    l.append([s,int(p),i+1])
l.sort(key=lambda x:(x[0],-x[1]))
[print(k) for i,j,k in l]
