tarou = hanako = 0
for _ in range(int(input())):
    s1, s2 = input().split()
    if s1 == s2:
        tarou += 1
        hanako += 1
    elif s1 > s2:
        tarou += 3
    else:
        hanako += 3
print(tarou, hanako)
