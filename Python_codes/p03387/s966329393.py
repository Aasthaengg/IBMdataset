ABC = list(map(int, input().split()))
ABC.sort()
count = ABC[2] - ABC[1]
other = ABC[2] - ABC[0] - count

if other % 2 == 0:
    count += other / 2
else:
    count += other // 2 + 2

print(int(count))