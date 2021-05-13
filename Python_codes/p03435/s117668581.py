C = [list(map(int, input().split())) for i in range(3)]

for a1 in range(0, 101):
    b1 = C[0][0] - a1
    b2 = C[0][1] - a1
    b3 = C[0][2] - a1
    if b1 < 0 or b2 < 0 or b3 < 0:
        continue
    a2 = C[1][0] - b1
    if a2 < 0 or C[1][1] - b2 != C[1][2] - b3 or C[1][1] - b2 != a2:
        continue
    a3 = C[2][0] - b1
    if a3 < 0 or a3 != C[2][1]- b2 or a3 != C[2][2] - b3:
        continue
    print ("Yes")
    exit()
print ("No") 