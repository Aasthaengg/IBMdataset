n = int(input())
Tarou = Hanako = 0
for i in range(n):
    a, b = map(str, input().split())
    if a > b: Tarou += 3
    elif a < b: Hanako += 3
    else:
        Tarou += 1
        Hanako += 1
print(Tarou, Hanako)
