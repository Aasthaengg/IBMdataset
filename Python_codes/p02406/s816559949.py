from sys import stdout
n = int(input())
i = 1

while True:
    x = i
    if x % 3 == 0:
        stdout.write(" " + str(i))
    else:
        while x:
            if x % 10 == 3:
                stdout.write(" " + str(i))
                break
            x //= 10
    i += 1
    if i > n: break
print()
