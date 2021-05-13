n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
d=[abs(a-b) for (a,b) in zip(x,y)]
for p in range(1,4):
    print(sum(map(lambda t: t**p,d))**(1/p))
print(max(d))
