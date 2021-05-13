a,b=input().split()
a=int(a)
b=int(b)
Hantei=(a * b) % 2
if Hantei == 1:
    print("Odd")
else:
    print("Even")
