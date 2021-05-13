n = int(input())

for i in range(10):
    if n > 1000:
        n -= 1000
    else:
        break

x = 1000 - n
print(x)