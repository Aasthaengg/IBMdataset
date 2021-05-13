N = int(input())

count = 0
for i in range(1, N + 1):
    count += i
    if count >= N:
        break

lv = list(range(1, i + 1))
elem = sum(lv) - N

for k in lv:
    if k != elem:
        print(k)