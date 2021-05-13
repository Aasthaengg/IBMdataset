import sys

count = 0

number = int(input())

for line in sys.stdin:
    n = int(line)
    if n == 2:
        count += 1
        continue

    if n % 2 == 0:
        continue

    jdg = True
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            jdg = False
            break
    if jdg:
        count += 1

print(count)

