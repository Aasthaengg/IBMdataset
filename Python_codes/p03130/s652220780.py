import sys

city = [0] * 4
for i in range(3):
    a, b = list(map(int, input().split()))
    city[a - 1] += 1
    city[b - 1] += 1
odd_count = 0
for count in city:
    if count % 2 == 1:
        odd_count += 1
        if odd_count > 2:
            print("NO")
            sys.exit()
print("YES")