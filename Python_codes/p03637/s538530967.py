n = int(input())
A = list(map(int, input().split()))

x = 0; y = 0
for a in A:
    if a % 2 == 1:
        x += 1
    elif a % 4 == 0:
        y += 1

if x <= y:
    print("Yes")
elif x == y + 1 and x + y == n:
    print("Yes")
else:
    print("No")
