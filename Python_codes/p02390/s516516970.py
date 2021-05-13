S=input()
h=S//3600	
s=S%3600
m=s//60
s=s%60
print ':'.join(map(str,[h,m,s]))