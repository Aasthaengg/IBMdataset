# diverta 2019 Programming Contest: B – RGB Boxes
R, G, B, N = [int(i) for i in input().split()]

bingo = 0

for r in range(N + 1):
    if R * r > N:
        break
    for g in range(N + 1):
        b = (N - (R * r + G * g)) // B
        if b < 0:
            break
        elif R * r + G * g + B * b == N:
            bingo += 1

print(bingo)