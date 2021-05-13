a=int(input())
b=int(input())
c=int(input())
x=int(input())
shurui = 0
for i in range(a+1):
  for j in range(b+1):
    for k in range(c+1):
      goukei=500*i+100*j+50*k
      if goukei == x:
        shurui +=1
print(shurui)