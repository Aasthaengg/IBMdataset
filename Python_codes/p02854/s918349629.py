import itertools
n = int(input())
a = list(map(int, input().split()))

a = list(itertools.accumulate(a))

target = a[-1]
for i in a:
    target = min(abs(a[-1] - i * 2), target)

print(target)