s = input()

n = int(s)

x = 1

for num in range(n):
    x *= num + 1
    x = x % ((1000000000) + 7)



print(x)
