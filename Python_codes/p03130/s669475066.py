route = [0 for num in range(4)]
for i in range(3):
    a, b = map(int, input().split())
    route[a - 1] += 1
    route [b - 1] += 1 
print('YES') if route.count(1) == 2 else print('NO')