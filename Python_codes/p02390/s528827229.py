s=int(input())
h=s//3600
s-=3600*h
m=s//60
s-=60*m
print(h,m,s,sep=":")
