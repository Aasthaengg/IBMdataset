a = 100000
for i in range(int(input())):
    a += (int(a * 0.05) + 999) // 1000 * 1000
print(a)