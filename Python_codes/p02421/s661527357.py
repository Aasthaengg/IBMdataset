N = int(input())
tarou = 0
hanako = 0
for _ in range(N):
    t,h = input().split()
    if t == h:
        tarou += 1
        hanako += 1
    elif [t,h] != sorted([t,h]):
        tarou += 3
    else:
        hanako += 3
print(tarou, hanako)
