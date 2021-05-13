c = [[0, 0, 0] for _ in range(3)]
for i in range(3):
    c[i] = list(map(int, input().split()))

for a1 in range(min(c[0])+1):
    b = [c[0][0] - a1, c[0][1] - a1, c[0][2] - a1]
    if c[1][0] - b[0] == c[1][1] - b[1] == c[1][2] - b[2]:
        if c[2][0] - b[0] == c[2][1] - b[1] == c[2][2] - b[2]:
            print("Yes")
            exit()
print("No")
