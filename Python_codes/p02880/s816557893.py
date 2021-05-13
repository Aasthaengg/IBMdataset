n=int(input())

for i in range(1,10):
    syou=n/i
    if syou.is_integer():
        if 1<=syou and syou<=9:
            print("Yes")
            exit()

print("No")