from itertools import combinations
while  True:
    n, x = [int(i) for i in input().split()]
    if n == x == 0: break
    count = 0
    array = set(range(1, n+1))
    for ele in combinations(array, 3):
        if sum(ele) == x:
            count += 1
    print(count)