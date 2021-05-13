n = int(input())
list = []
for _ in range(n):
    list.append(input())

sets = set(list)
ans = len(sets)

print(ans)