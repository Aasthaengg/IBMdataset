k = int(input())

l = [0]
for i in range(1, k + 1):
    l.append(l[-1] + i // 2)
# l = [0, 0, 1, 2, 4, 6, 9, 12, ... k]

print(l[-1])