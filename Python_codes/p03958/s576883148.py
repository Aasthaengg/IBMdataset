k, t = map(int, input().split())
a = [int(i) for i in input().split()]
s = sum(a)
print(max(0, max(a) - (s-max(a)) - 1))
