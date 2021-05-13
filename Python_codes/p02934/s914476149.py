n = input()
a = list(map(int, input().split()))
b = 0
for i in a:
    b += i ** (-1)
print(b ** (-1)) 