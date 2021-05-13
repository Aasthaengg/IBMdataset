from collections import Counter


N = int(input())
a = Counter(map(lambda x: min(8, int(x) // 400), input().split()))
super_coders = a.pop(8, 0)
mn = len(a)
if mn == 0 and super_coders:
    mn = 1
mx = len(a) + super_coders
print(mn, mx)
