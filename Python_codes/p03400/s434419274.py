n=int(input())
d,x=map(int,input().split())
eat=[]
for i in range(n):
    a=int(input())
    count=0
    for j in range(101):
        aeat=a*j+1
        if aeat<=d:
            count+=1
        else:
            eat.append(count)
            break
print(x+sum(eat))
