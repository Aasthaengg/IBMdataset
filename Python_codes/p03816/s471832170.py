N = int(input())
A = list(map(int, input().split(" ")))
A.sort()
counter = {}

for a in A:
    if a in counter:
        counter[a] += 1
    else:
        counter[a] = 1

one, two = 0, 0
for c in counter:
    if counter[c] % 2 == 0:
        two += 1
    else:
        one += 1

print(one + two - (two % 2))