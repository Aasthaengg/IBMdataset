n = int(input())

a = [0] * n
for i in range(n):
    a[i] = int(input())

for i in range(n):
    if a[i] %2 == 0:
        continue
    else:
        print("first")
        exit()

print("second")