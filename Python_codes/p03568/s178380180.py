N = int(input())
array = list(map(int, input().split()))
all_pattern = 3 ** N
count = 0
for x in array:
    if x % 2 == 0:
        count += 1
odd_pattern = 2**count
print(all_pattern - odd_pattern)
