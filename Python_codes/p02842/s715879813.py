n = int(input())
x = int(n / 1.08 - 2)
for i in range(x, x + 4):
    if int(i * 108 // 100) == n:
        print(i)
        break
else:
    print(":(")