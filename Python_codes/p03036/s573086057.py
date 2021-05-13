number = input().split(" ")
r = int(number[0])
D = int(number[1])
x = int(number[2])

for i in range(1,11):
    x = r*x - D
    print(x)