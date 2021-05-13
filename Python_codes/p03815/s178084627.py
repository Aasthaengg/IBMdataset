x=int(input())

q,r = divmod(x,11)

if r==0:a=0
elif r <= 6:a = 1
else:a = 2
  
print(2*q+a)