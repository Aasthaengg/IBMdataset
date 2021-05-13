n = [int(i) for i in input().split()]

a = n[0]
b = n[1]

if (a % 2 == 0) or (b % 2 == 0):
    print("Even")
else:
    print("Odd")