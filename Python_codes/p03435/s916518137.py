c = []
for i in range(3):
    c.append(list(map(int, input().split(" "))))

f = "No"
for a1 in range(101):
    for a2 in range(101):
         for a3 in range(101):
            if (c[0][0] - a1 == c[0][1] - a2 == c[0][2] - a3
                and c[1][0] - a1 == c[1][1] - a2 == c[1][2] - a3
                and c[2][0] - a1 == c[2][1] - a2 == c[2][2] - a3):
                f = "Yes"

print(f)