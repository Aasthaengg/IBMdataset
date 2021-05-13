import math

n=int(input())
x=input().split()
y=input().split()
A=[]
# case p=1
su=0
i=0
while i<n:
    su+=math.sqrt((int(x[i])-int(y[i]))*(int(x[i])-int(y[i])))
    i+=1
A.append(su)

# case p=2
su2=0
l=0
while l<n:
    su2+=(int(x[l])-int(y[l]))*(int(x[l])-int(y[l]))
    l+=1
A.append(math.sqrt(su2))

# case p=3
su3=0
m=0
while m<n:
    su3+=math.pow(math.sqrt(math.pow(int(x[m])-int(y[m]),2)),3)
    m+=1
A.append(math.pow(su3,1/3))

# case p=mugendai
mu=[]
q=0
while q<n:
    mu.append(math.sqrt(math.pow(int(x[q])-int(y[q]),2)))
    q+=1
M=max(mu)
A.append(M)

for Ans in A:
    print(Ans)

