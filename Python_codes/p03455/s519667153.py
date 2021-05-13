# 1 <= a , b <= 10000

a,b = input().split()

total = int(a) * int(b)

if total % 2 == 0:
    print("Even")
else:
    print("Odd")