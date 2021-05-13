a, b = map(int, input().split())

x = a * b
z = x % 2
if z == 0 :
    print("Even")
else :
    print("Odd")