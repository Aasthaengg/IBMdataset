n , m = map(int, input().split())
lis = list(map(int, input().split()))

total = 0

for i in lis:
    if i >= m:
        total += 1

print(total)