n = int(input())
a = input()
b = input()
c = input()

ans = 0
for x, y, z in zip(a, b, c):
    if x == y == z:
        continue
    elif x == y or y == z or z == x:
        ans += 1
    else:
        ans += 2

print(ans)
