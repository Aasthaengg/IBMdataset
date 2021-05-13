from itertools import combinations

N = int(input())
a = list(map(int, input().split()))
count = 0
for i in combinations(a,3):
    b = list(i)
    b.sort()
    if b[2] > b[1] and b[1] > b[0]:
        if b[2] < (b[1] + b[0]):
            count += 1

print(count)