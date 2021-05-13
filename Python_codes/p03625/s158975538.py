from collections import Counter
input()
angles = sorted(((key, value) for key, value in Counter(map(int, input().split())).items() if value > 1), key=lambda t: t[0])
try:
    square = angles[-1][0] ** 2 if angles[-1][1] > 3 else angles[-1][0] * angles[-2][0]
except:
    square = 0
print(square)