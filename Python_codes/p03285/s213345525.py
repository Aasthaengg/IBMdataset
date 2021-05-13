n = int(input())

count = 0

for i in range(26):
    for j in range(15):
        if 4 * i + 7 * j == n:
            count += 1
            break
        else:
            pass

if count == 0:
    print("No")
else:
    print("Yes")