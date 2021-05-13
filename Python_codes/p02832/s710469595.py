n = int(input())
j = 1

for i in map(int, input().split()):
    if i == j:
        j += 1

print((-1, n - j + 1)[j != 1])