N = int(input())
a = list(map(int, input().split()))

total = 0
for num in a:
    count = 0
    while num % 2 == 0:
        count += 1
        num //= 2
    total += count

print(total)