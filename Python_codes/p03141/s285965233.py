N=int(input())
net=[]
y=0
for i in range(0,N):
    a,b=map(int,input().split())
    y+=b
    net.append(a+b)

net.sort(reverse=True)

t=sum(net[i] for i in range(0,N) if i%2==0)
print(t-y)