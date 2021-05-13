n=int(input())
a=[]
while(n%2==0):
    a.append(2)
    n=n/2
for i in range(3,int((n**0.5))+1,2):
    while(n%i==0):
        a.append(i)
        n=n/i
if(n>2):
    a.append(int(n))
l=list(set(a))
c=1
t=0
for i in range(len(l)):
    while(0.5*(c*(c+1))<=a.count(l[i])):
        t=t+1
        c=c+1
    c=1
print(t)