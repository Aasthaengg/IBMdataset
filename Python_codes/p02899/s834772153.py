n = int(input())
a = list(map(int, input().split()))
order = []
for i in range(n):
    order.append((i + 1, a[i]))
order.sort(key=lambda x: x[1])
print(" ".join(list(map(lambda x: str(x[0]), order))))