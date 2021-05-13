a, b = input().split()
a = int(a)
b = int(b)

if a <= b:
    print("0")
elif a <= b*2:
    print("0")
else:
    print(a-b*2)