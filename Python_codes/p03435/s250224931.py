# input
C = [list(map(int, input().split())) for i in range(3)]

# check
base = [C[0][0], C[1][1], C[2][2]]
case_AB = [
    1
    for a in range(base[0] + 1)
    for b in range(base[1] + 1)
    for c in range(base[2] + 1)
    if [
        [base[0], b + (base[0] - a), c + (base[0] - a)],
        [a + (base[1] - b), base[1], c + (base[1] - b)],
        [a + (base[2] - c), b + (base[2] - c), base[2]]
    ] == C
]

if case_AB:
    print("Yes")
else:
    print("No")