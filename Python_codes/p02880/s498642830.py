n = int(input())
x = 1
for i in range(9):
    if n/(i+1) == int(n/(i+1)):
        if n/(i+1) <= 9:
            x = 0
print("Yes" if x == 0 else "No")