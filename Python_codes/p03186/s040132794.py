instr = input()
A, B, C = map(int, instr.split(" "))

score = 0
if B < C:
    score += 2 * B
    C -= B
    B = 0

    if A <= C:
        score += A
        C -= A
        A = 0

        if C > 0:
            score += 1
            C -= 1

    else:
        score += C
        C = 0
        A -= C
else:
    score += B + C
    B = C = 0

print(score)