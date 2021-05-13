x=int(input())

h=int(x//3600)
m=int(x%3600//60)
s=int(x%60)

print(h,':',m,':',s,sep='')
