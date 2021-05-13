n = int(input())
x = int(n**0.5)
while n%x!=0: x-= 1
y = n//x
print(x-1+y-1)