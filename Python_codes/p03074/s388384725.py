n,k=map(int,input().split())
s=list(input())
count0=[]
count1=[]
if s[0]=="0":
    count1.append(0)

i=0
temp=0
while i<=n-1:
    j=0
    while i+j+1<=n-1 and s[i+j]==s[i+j+1]:
        j+=1
    if s[i]=="0":
        count0.append(j+1)
    else:
        count1.append(j+1)
    i+=(j+1)


if s[-1]=="0":
    count1.append(0)


sun=sum(count0[:k])+sum(count1[:k+1])
temp=sun
for i in range(len(count0)-k):
    sun=sun+count0[k+i]+count1[k+1+i]-count0[i]-count1[i]
    temp=max(temp,sun)
print(temp)