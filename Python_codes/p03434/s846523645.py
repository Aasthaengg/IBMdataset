N=int(input())
a=list(map(int,input().split()))
a.sort()
a.reverse()
b=[]
if len(a)%2==0:
    for i in range(0,(len(a)//2)):
        b.append(a[2*i]-a[2*i+1])
else:
    for i in range(0,(len(a)//2)):
        b.append(a[2*i]-a[2*i+1])
    b.append(a[len(a)-1])
print(sum(b))