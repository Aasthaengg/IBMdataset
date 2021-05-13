n=int(input())
p=n//11
if 11*p==n:print(p*2)
elif 11*p+6>=n:print(p*2+1)
else:print(p*2+2)