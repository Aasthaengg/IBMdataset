n = int(input())
a = [int(i) for i in input().split()]
d = {1 : 0, 2 : 0, 4 : 0}
for i in a:
    if i % 4 == 0:
        d[4] += 1
    elif i % 2 == 0:
        d[2] += 1
    else:
        d[1] += 1
if d[1] <= d[4]:
    print("Yes")
elif d[1] - d[4] == 1 and d[2] == 0:
    print("Yes")
else:
    print("No")