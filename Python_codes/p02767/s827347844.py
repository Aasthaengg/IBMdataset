n=int(input())
x=list(map(int,input().split()))
c=[]
for i in range(101):
    b=0
    for j in x:
        b+=((j-i)**2)
    c.append(b)
print(min(c))