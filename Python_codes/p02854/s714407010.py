n=int(input())
a=list(map(int,input().split()))
def Csum(a):
    b,c=[0],0
    for i in range(len(a)):
        c+=a[i]
        b.append(c)
    return b
b=Csum(a)
c=sum(a)
d=[]
for i in range(1,n):
    d.append(abs((c-b[i])-b[i]))
print(min(d))