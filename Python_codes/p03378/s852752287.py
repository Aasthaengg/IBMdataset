a,b,c=map(int,input().split())
b=list(map(int,input().split()))
i=c
total=0
total2=0
while True:
    i+=1
    if i in b:
        total+=1
    if i==a:
        break
i=c
while True:
    i-=1
    if i in b:
        total2+=1
    if i==0:
        break
print(min(total,total2))