import itertools
N = int(input())
A = list(map(int, input().split()))

mini = float('inf')

cumsum = list(itertools.accumulate(A))
A.reverse()
rev = list(itertools.accumulate(A))
rev.reverse()
cumsum.pop()
rev.pop(0)

for i, j in zip(cumsum,rev):
    if abs(i-j) < mini:
        mini = abs(i-j)

print(mini)