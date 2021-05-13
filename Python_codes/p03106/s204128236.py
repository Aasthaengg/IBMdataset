a,b,k=map(int,input().split())
x=min(a,b)
l=[]
for i in range(1,x+1):
    if a%i==0 and b%i==0:
        l.append(i)
y=len(l)
print(l[y-k])