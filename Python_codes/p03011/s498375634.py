import itertools
val = 0
for i in itertools.permutations(list(map(int, input().split())), 2):
    if val == 0:
        val = sum(i)
    else:
        val = min(sum(i), val)
print(val)
