c = [list(map(int, input().split())) for _ in range(3)]

c0 = [c[0][0]-c[0][1], c[0][0]-c[0][2], c[0][1]-c[0][2]]
c1 = [c[1][0]-c[1][1], c[1][0]-c[1][2], c[1][1]-c[1][2]]
c2 = [c[2][0]-c[2][1], c[2][0]-c[2][2], c[2][1]-c[2][2]]

if c0 == c1 == c2:
    print("Yes")
else:
    print("No")