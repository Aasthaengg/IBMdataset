from collections import Counter

N = int(input())
S = input()
counter_s = Counter(S)
min_stone = counter_s.most_common()[-1][1]
if min_stone == N:
    min_stone = 0
A, B = 0, counter_s['.']
for s in S:
    if s == '#':
        A += 1
    else:
        B -= 1
    if min_stone > A+B:
        min_stone = A+B
print(min_stone)