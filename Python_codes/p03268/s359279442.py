a,b=map(int,input().split())
c=a//b
print((c**3)+((a-b//2)//b+1)**3*(1-b%2))