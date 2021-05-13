T, H = 0, 0
for i in range(int(input())):
    a, b = input().split()
    if a == b:
        T, H = T + 1, H + 1
    if a < b:
        H += 3
    if a > b:
        T += 3
print(T, H)