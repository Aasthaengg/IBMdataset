N = input()
number_list = [int(i) for i in input().split()]
sorted_list = sorted(number_list)
count = 0
for i,j in zip(number_list, sorted_list):
    if i != j:
        count += 1

if count == 2 or count == 0:
    print('YES')
else:
    print('NO')