a,b=input().split()
b=b.replace('.','')
a,b=list(map(int,[a,b]))
ans=a*b
print(ans//100)