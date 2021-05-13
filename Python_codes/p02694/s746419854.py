from decimal import Decimal
X=int(input())
M=100
i=0

while M<X:
  M=(M*101)//100
  i+=1
  
print(i)