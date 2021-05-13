N=input()
a=[]
s=len(N)

for i in range(s-1,-1,-1):
    a.append(int(N[i]))
a.append(0)
#print(a)

p=sum(a)
t=0
f=0
c=0
for i in range(len(a)-1):
    if a[i] <= 5:
        t+=a[i]
        if a[i] == 5 and a[i+1]>=5:a[i+1]+=1
        f=0
        
    else:
        c+=10-a[i]
        a[i+1] += 1
        f=1
        
print(t+f+c)