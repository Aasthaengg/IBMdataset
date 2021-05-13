n = int(input())
a = list(map(int,input().split()))
four, two, none = 0, 0, 0
for i in range(n):
    if a[i] % 4 == 0:
        four += 1
    elif a[i] % 2 == 0:
        two += 1
    else:
        none += 1
if four >= none or (four == none-1 and two == 0):
    print("Yes")
else:
    print("No")