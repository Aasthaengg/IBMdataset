n = int(input())
a, b = map(int, input().split())
pli = list(map(int, input().split()))

one = [p for p in pli if p<=a]
two = [p for p in pli if (a+1)<=p<=b]
the = [p for p in pli if (b+1)<=p]

print(min([len(one), len(two), len(the)]))
