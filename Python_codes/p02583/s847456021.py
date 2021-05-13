import itertools

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
count = 0
for i in itertools.combinations(arr, 3):
    if i[0] + i[1] > i[2] and i[0] + i[2] > i[1] and i[2] + i[1] > i[0] and i[0] != i[1] != i[2]:
        count += 1
print(count)


