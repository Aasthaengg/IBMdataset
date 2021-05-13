a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
d=0
for i in range(1,a+1):
  if b<=(i//10000+(i//1000-(i//10000)*10))+(i//100-(i//1000)*10)+(i//10-(i//100)*10)+(i//1-(i//10)*10)<=c:
    d=d+i
print(d)
