s=input().split()
a=int(s[0])
b=int(s[1])
c=int(s[2])
k=0
for i in range(a,b+1):
   if  c%i==0:
       k+=1
print("{0}".format(k))