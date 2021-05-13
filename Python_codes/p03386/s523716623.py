a,b,k=map(int,input().split())
t=set()
for i in range(a,min(a+k,b+1)):
    t.add(i)
for i in range(max(a,b-k+1),b+1):
    t.add(i)
a=list(t)
a.sort()
for i in a:
    print(i)