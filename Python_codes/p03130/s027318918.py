ab = [list(map(int, input().split())) for i in range(3)]
one, two, three, four = 0, 0, 0, 0
for i in ab:
    one += i.count(1)
    two += i.count(2)
    three += i.count(3)
    four += i.count(4)
if one == 3 or two == 3 or three == 3 or four == 3:
    print("NO")
else:
    print("YES")