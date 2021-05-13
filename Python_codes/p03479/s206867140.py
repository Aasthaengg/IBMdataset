x, y = map(int, input().split())
c=0
while(1):
   if y>=x:
       c+=1
       x*=2
   else:
       break
print(c)