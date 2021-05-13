n=int(input())

x=list(map(int,input().split()))
y=list(map(int,input().split()))
p=[0]*4

for i in range(n):
    p[0]+=abs(x[i]-y[i])
    p[1]+=abs(x[i]-y[i])**2
    p[2]+=abs(x[i]-y[i])**3
    p[3]=max(p[3],abs(x[i]-y[i]))
p[1]=p[1]**(1/2)
p[2]=p[2]**(1/3)
for i in range(4):
    print("{0:.5f}".format(p[i]))

