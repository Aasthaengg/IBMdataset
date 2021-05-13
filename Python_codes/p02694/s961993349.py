import math
score = int(input())
answer = 100
year = 0
while answer < score:
    answer += answer//100
    year += 1
print(year)