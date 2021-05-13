n,m=map(int, input().split())

ans=0
m2=2**m
for i in range(1, 10**4):
    ans+=(100*(n-m)+1900*m)*i*((1-1/m2)**(i-1))/m2
print(int(ans+0.1))
