n = input()

for i in range(3):
    if n[i] != n[3-i-1]:
        print("No")
        exit(0)

print("Yes")