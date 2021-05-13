z=list(map(int,input().split()))
x=list(map(int,input().split()))
d={}
c=0
for i in x:
       if d.get(i,0)==0:
              c+=i
if c>=z[0]:
       print("Yes")
else:
       print("No")

       
