a,b=map(int,input().split())
x=0
for i in range(1,10000000000):
    if b*i%a==0:
        x=i
        break
    elif b*i==b*a:
        x=a
        break
print(b*x)