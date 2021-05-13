n = int(input())
d = [list(input().split()) for _ in range(n)]

c = 0

for i in range(n):
    if d[i][0] == d[i][1]:
        c += 1
    else:
        c = 0
    if c == 3:
        break

if c == 3:
    print("Yes")
else:
    print("No")