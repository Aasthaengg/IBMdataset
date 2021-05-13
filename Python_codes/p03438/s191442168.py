N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

import math

count_1up = 0
count_2up = 0

for a, b in zip(A, B):
    if a - b >= 0:
        count_1up += a - b
    else:
        count_2up += math.ceil((b - a) / 2)

diff = sum(B) - sum(A)

# print(diff, count_1up, count_2up)
if diff < 0:
    print("No")
elif diff < count_1up or diff < count_2up:
    print("No")
else:
    print("Yes")