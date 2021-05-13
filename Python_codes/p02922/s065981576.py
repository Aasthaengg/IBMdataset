import math as m

a,b= map(int, input().split())
x = m.ceil((b-1)/(a-1))
print(x)