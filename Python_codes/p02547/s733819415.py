n = int(input())
t = 0
f = False
for i in range(n):
    a,b = map(int, input().split())
    if a == b:
        t += 1
    else:
        t = 0
    if t>= 3:
        f = True
        # break

if f:
    print("Yes")
else:
    print("No")


