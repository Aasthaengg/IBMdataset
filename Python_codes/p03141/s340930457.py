n = int(input())

dishes = []
for _ in range(n):
    a, b = map(int, input().split())
    dishes.append((a+b, a, b))
dishes.sort(reverse=True)

T = A = 0
for i, (_, a, b) in enumerate(dishes):
    if not i & 1:
        T += a
    else:
        A += b
print(T-A)
