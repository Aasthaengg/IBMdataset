coordinate_lst = []
for _ in range(5):
    coordinate_lst.append(int(input()))
k = int(input())

coordinate_lst.sort()
max_distance = coordinate_lst[-1] - coordinate_lst[0]

if max_distance <= k:
    print('Yay!')
else:
    print(':(')
