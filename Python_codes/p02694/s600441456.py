x = int(input())
a = 100
i = 0
while True:
    i += 1
    a = a * 101 // 100
    if x <= a:
        break
print(i)