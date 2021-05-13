a,b=map(int,input().split())

m=b/a

if m-int(m) == 0: 
 print(a+b)
else:
 print(b-a)