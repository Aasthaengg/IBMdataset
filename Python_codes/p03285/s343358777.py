n = int(input())

f = False

for i in range(26):
    for j in range(15):
        if 4 * i + 7 * j == n:
            f = True
            break
        else:
            pass

if f:
    print("Yes")
else:
    print("No")