import math
n=int(input())
p=[]
for x in range(2,5555):
    t=True
    for y in range(2,math.ceil(math.sqrt(x))+1):
        if x%y==0:t=False
    if t:p.append(x)
c=0
ans=[]
for i in range(len(p)):
    if p[i]%5==1:
        ans.append(p[i])
        c+=1
    if c==n:break
s=''
for x in ans:
    s+=str(x)+' '
print(s)