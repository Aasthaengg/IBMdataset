A, B, C = sorted(map(int, input().split()))
count = 0

diff = C - B
count += diff
A += diff
B += diff

if (B - A) % 2 == 0:
    count += (B - A) // 2
else:
    count += (B - A) // 2 + 2

print(count)