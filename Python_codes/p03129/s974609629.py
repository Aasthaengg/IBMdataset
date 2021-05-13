a,b = list(map(int, input().split()))
if a % 2 == 0:
    if a / 2 >= b:
        print("YES")
    else:
        print("NO")
else:
    if (a + 1) / 2 >= b:
        print("YES")
    else:
        print("NO")
