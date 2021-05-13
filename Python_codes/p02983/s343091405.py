a,b=map(int,input().split())
if b-a>=2019:
    print(0)
    exit()
d=[]
for i in range(a,b+1):
    if i%2019==0:
        print(0)
        exit()
    for j in range(a,b+1):
        if i<j:
            d.append((i*j)%2019)
print(min(d))