N = int(input())
A = input()
B = input()
C = input()
ans = 0
for x, y, z in zip(A, B, C):
    x, y, z = sorted([x, y, z])
    if x != y and y != z:
        ans += 2
    elif x == y and y != z:
        ans += 1
    elif x != y and y == z:
        ans += 1
print(ans)