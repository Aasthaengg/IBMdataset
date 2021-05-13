a,b,c,k=map(int,input().split())
Unfair=10**18

if k==0:
    print(a-b)
    exit()
elif k%2==0:
    k=2
else:
    k=1

for i in range(k):
    a2=b+c
    b2=a+c
    c2=a+b
    a,b,c=a2,b2,c2

if a-b>Unfair:
    print("Unfair")
else:
    print(a-b)