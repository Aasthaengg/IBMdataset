n = int(input())
a = list(map(int, input().split()))
o = 0
t = 0
f = 0
for i in a:
    if i % 4 == 0:
        f += 1
    elif i % 2 == 0:
        t += 1
    else:
        o += 1
if t > 0:
    print("Yes" if f >= o else "No")
else:
    print("Yes" if f >= o - 1 else "No")