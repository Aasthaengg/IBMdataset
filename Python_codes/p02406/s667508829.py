import sys

n = int(input())
for i in range(1, n + 1):
    if i % 3 == 0:
        sys.stdout.write(' ')
        sys.stdout.write(str(i))
    else:
        x = i
        for j in range(0, 5):
            if x % 10 == 3:
                sys.stdout.write(' ')
                sys.stdout.write(str(i))
                break
            x //= 10

print('')