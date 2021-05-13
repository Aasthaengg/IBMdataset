N=int(input())
a=list(map(int,input().split()))
me=sum(a)/len(a)
l=[]
for i in range(N):
    l.append([abs(me-a[i]),i])
l.sort(key=lambda x:x[0])
print(l[0][1])

