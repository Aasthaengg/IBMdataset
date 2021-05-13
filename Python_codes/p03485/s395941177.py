a,b = map(int,input().split())

u = (a+b)
x = (a+b) // 2 

if u % 2 > 0:
    x = x + 1

print(str(x))