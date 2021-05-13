a=[]
for i in range(5):
    a.append(int(input()))

zako=9
switch=0
for i in range(5):
    b=a[i]%10
    if b<=zako and b!=0:
        zako=b
        memory=i
        switch=1

if switch==0:
    memory=1
x=a.pop(memory)

lst=[]

for i in range(4):
    c=a[i]//10
    c=c*10
    if a[i]%10!=0:
        c+=10
    lst.append(c)

print(x+sum(lst))