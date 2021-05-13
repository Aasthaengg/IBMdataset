from collections import Counter

N = int(input())
arr = input()
west_side = Counter()
east_side = Counter(arr)
costs = []

for i in range(N):
    leader = arr[i]
    east_side[leader] -= 1

    costs.append(west_side['W'] + east_side['E'])
    west_side[leader] += 1

print(min(costs))
