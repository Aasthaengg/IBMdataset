n = int(input())
a = input()
b = input()
c = input()
ans = 0

for i in range(n):
    x = a[i]
    y = b[i]
    z = c[i]

    if x == y == z:
        continue
    elif x != y and y != z and z != x:
        ans += 2
    else:
        ans += 1

print(ans)