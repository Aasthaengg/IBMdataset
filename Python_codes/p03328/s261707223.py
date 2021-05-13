a,b=map(int,input().split())
n=b-a
high=1
for i in range(2,n):
    high+=i

print(high-a)