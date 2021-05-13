a, b, m = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
min_cost = min(a_list) + min(b_list)

for _ in range(m):
    x, y, c = map(int, input().split())
    _a = a_list[x-1]
    _b = b_list[y-1]
    cost = _a + _b - c
    min_cost = min(cost, min_cost)
print(min_cost)

