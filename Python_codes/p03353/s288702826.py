s=list(input())
k=int(input())
n=len(s)
x=[]
for i in range(n):
    x.append(s[i])
if n>=2:
    for i in range(n-1):
        z=s[i]+s[i+1]
        x.append(z)
if n>=3:
    for i in range(n-2):
        z=s[i]+s[i+1]+s[i+2]
        x.append(z)
if n>=4:
    for i in range(n-3):
        z=s[i]+s[i+1]+s[i+2]+s[i+3]
        x.append(z)
if n>=5:
    for i in range(n-4):
        z=s[i]+s[i+1]+s[i+2]+s[i+3]+s[i+4]
        x.append(z)
x=set(x)
x=sorted(x)
print(x[k-1])
