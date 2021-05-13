from itertools import combinations

coord = []
for _ in range(5):
    coord.append(int(input()))
k = int(input())

for i, j in combinations(coord, 2):
    if j - i > k:
        print(':(')
        break
else:
    print('Yay!')
