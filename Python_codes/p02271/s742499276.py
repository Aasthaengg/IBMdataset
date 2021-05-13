from itertools import combinations

n = int(input())
a_array = [int(x) for x in input().split()]
q = int(input())
m_array = [int(x) for x in input().split()]

array = []
for j in range(n + 1):
    x = combinations(a_array, j)
    for y in x:
        array.append(sum(y))

for m in m_array:
    print("yes" if m in array else "no")
