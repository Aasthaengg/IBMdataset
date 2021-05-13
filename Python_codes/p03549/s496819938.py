n,m=map(int,input().split())
time=100*(n-m)+1900*m
a=2**(-m)
b=1-a
ans=1/(1-b)**2
ans*=time*a
print(int(ans))