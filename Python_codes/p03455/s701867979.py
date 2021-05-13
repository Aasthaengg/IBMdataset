list = input().split()
a=int(list[0])
b=int(list[1])

c = a*b

if c%2==1:
    print("Odd")

if c%2==0:
    print("Even")
