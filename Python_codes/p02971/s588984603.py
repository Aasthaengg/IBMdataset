from copy import deepcopy
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
b = deepcopy(a)

first_max = max(b)
b.remove(first_max)
second_max = max(b)

for x in a:
    if x == first_max:
        print(second_max)
    else:
        print(first_max)
