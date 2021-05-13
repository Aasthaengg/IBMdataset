n = int(input())
for i in range(n, -1, -1):
    temp = i ** 0.5
    if temp == int(temp):
        print(i)
        break