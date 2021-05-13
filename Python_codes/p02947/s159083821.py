import collections
n = int(input())

s = ["".join(sorted(input())) for _ in range(n)]

listcount = collections.Counter(s)

print(sum((i-1)*i//2 for i in listcount.values()))