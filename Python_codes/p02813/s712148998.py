import itertools
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
for i, s in enumerate(list(itertools.permutations(list(range(1, n+1))))):
    if list(s) == p:
        a = i
    if list(s) == q:
        b = i
print(abs(a-b))
