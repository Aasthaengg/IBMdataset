n = int(input())

for i in range(n):
    a = int(input())
    if a % 2 == 1:
        print("first")
        exit(0)

print("second")
