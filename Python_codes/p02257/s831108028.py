n=int(input())
c=0
for _ in range(n):
 x=int(input())
 if 1 in [x-1,pow(2,x-1,x)]:c+=1
print(c)
