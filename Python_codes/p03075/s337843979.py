import itertools

antenna = [int(input()) for _ in range(5)]
k = int(input())

count = 0
for p in itertools.permutations(antenna, 2):
    x, y = p
    if abs(x - y) > k:
        count += 1

if count == 0:
    print('Yay!')
else:
    print(':(')