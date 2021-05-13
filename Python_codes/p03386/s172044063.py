a,b,k=map(int,input().split())
l=[]
for i in range(a,min(b+1,a+k)):
    l.append(i)
for i in range(max(a,b-k+1),b+1):
    l.append(i)
l=sorted(set(l))
for i in l:print(i)