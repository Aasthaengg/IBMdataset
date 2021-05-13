n, m = map(int, input().split())
a = set(range(1, m + 1))
for _ in range(n):
    a &= set(list(map(int, input().split()))[1:])
print(len(a))
