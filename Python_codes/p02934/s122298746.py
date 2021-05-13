n = int(input())
a = list(map(int, input().split()))
s = sum([1 / x for x in a])
print(1 / s)
