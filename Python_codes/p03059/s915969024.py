a,b,t=map(int,input().split())
a=float(a)
t=float(t)
j=a
c=0
n=2.0
while True:
    if j<=t+0.5:
        c+=b
        j=a*n
        n+=1.0
    else:
        break
print(c)