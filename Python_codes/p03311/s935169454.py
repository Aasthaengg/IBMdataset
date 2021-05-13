n = int(input())
a = [ai - i for i, ai in enumerate(map(int, input().split()), 1)]
a.sort()
med = a[len(a)//2]
print(sum(abs(ai - med) for ai in a))