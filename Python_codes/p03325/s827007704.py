N = int(input())

an = list(map(int, input().split()))

count = 0
for a in an:
    while True:
        if a % 2 != 0:
            break
        a = a /2
        count += 1

print(count)
