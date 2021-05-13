from collections import defaultdict


N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

problemsinHand = defaultdict(int)
problemsNeeded = defaultdict(int)

for d in D:
    problemsinHand[d] += 1
for t in T:
    problemsNeeded[t] += 1

for key, value in list(problemsNeeded.items()):
    if value > problemsinHand[key]:
        print('NO')
        quit()

print('YES')