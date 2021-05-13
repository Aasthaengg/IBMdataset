n, m = map(int, input().split())
food = {i+1 for i in range(m)}

for i in range(n):
    k, *l = map(int, input().split())
    food = set(l) & food

print(len(food))