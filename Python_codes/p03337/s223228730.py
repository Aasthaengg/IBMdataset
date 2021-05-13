a,b = map(int,input().split())
x = a +b
y = a- b
z = a*b
maxNumber = x
if maxNumber < y:
    maxNumber = y
if maxNumber < z:
    maxNumber = z
print(maxNumber)
