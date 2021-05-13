S = input().strip()

for i in range(6):
    if S == "hi" * (i + 1):
        print("Yes")
        exit()

print("No")
