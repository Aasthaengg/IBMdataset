from itertools import combinations

# input
antennas = []
a_append = antennas.append
for i in range(5):
    a_append(int(input()))

k = int(input())

# check
pattern = list(combinations(antennas, 2))
max_len = max(
    [
        abs(i - j)
        for i, j in pattern
    ]
)
if max_len <= k:
    print("Yay!")
else:
    print(":(")