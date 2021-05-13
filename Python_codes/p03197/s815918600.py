n = int(input())
for i in range(n):
    p = int(input())
    if p % 2 == 0:
        continue
    else:
        print("first")
        exit()

print("second")