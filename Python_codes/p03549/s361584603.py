import math

N,M=map(int,input().split())
ans=0
for i in range(1,100000):
    ans+=i*(1900*M+(N-M)*100) * (0.5)**M * (1-(0.5)**M)**(i-1)

a=math.floor(ans)
b=math.ceil(ans)

if abs(a-ans)>abs(b-ans):
    print(b)
else:
    print(a)