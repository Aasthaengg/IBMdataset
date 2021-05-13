from itertools import combinations
N = int(input())
scores = [int(input())for i in range(N)]
sums= sum(scores)
if sums % 10 != 0:
    print(sums)
    exit()
scores.sort()
for i in range(N):
    if (sums-scores[i]) % 10 != 0:
        print(sums - scores[i])
        exit()
print(0)