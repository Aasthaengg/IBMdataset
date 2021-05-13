a,b,k=map(int,input().split())
l=[0]
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        l.append(i)
l.sort()
l.reverse()
print(l[k-1])