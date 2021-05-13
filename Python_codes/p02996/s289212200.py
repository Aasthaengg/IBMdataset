n = int(input())

ab = [list(map(int, input().split())) for _ in range(n)]

ab.sort(key=lambda x: x[1])

s = 0

flag = True

for a, b in ab:
    s += a
    if s > b:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")