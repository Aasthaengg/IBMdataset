N = int(input())

count = int(0)
g = N

while g >= 3:
    g = g - 3
    count = count + 1

print(count)