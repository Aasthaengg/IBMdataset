a, b = input().split()
for i in range(320):
    if int(a + b) == i * i:
        print("Yes")
        exit()
print("No")