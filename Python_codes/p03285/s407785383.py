a = int(input())

for i in range(7):
    b = a - i*4
    if b >= 0 and b % 7 ==0:
        print("Yes")
        exit()

print("No")