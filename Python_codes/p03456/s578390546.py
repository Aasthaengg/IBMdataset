a,b = input().split()

a = int(a+b)

for i in range(1000000):
    if i ** 2 == a:
        print("Yes")
        exit(0)
else:
    print("No")