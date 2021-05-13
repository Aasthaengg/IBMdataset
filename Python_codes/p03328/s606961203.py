a,b=map(int,input().split())
dif=b-a
high=0
for i in range(1,dif+1):
    high+=i
print(high-b)