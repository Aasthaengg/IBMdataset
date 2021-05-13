x1 = input().split(" ")
x2 = [int(i) for i in x1]


x3 = x2[0]*x2[1]

if x3 % 2 == 0:
    print("Even")
elif x3 % 2 == 1:
    print("Odd")
