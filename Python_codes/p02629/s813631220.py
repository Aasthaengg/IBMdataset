n = int(input())
char = list("abcdefghijklmnopqrstuvwxyz")
name = ""
while n > 0:
    n -= 1
    name = char[n % 26] + name
    n = n // 26
print(name)