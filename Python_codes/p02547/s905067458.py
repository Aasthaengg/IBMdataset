n = int(input())

count = 0
for _ in range(n):
    a, b = input().split()
    if a == b:
        count += 1
    else:
        count = 0
    if count == 3:
        print("Yes")
        quit()

print("No")
