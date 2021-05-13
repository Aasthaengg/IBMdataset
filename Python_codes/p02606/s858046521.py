L, R, d = [int(x) for x in input().split()]

count = 0

for i in range(L, R + 1):
    if i % d == 0:
        count = count + 1

print(count) 