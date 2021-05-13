n = int(input())
a = []
b = []
for _ in range(n):
    at,bt = [int(x) for x in input().split()]
    a.append(at)
    b.append(bt)

print(max(a)+min(b))