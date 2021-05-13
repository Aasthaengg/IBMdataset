n = int(input())

for num in range(n, 1000):
    if num % 111 == 0:
        print(num)
        break