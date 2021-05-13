abcd = list(input())

for bit in range(1 << 3):
    answer = 0
    op = ["-", "-", "-"]
    for i in range(3):
        if (bit >> i) & 1:
            op[i] = "+"
    if eval(abcd[0] + op[0] + abcd[1] + op[1] + abcd[2] + op[2] + abcd[3]) == 7:
        answer = abcd[0] + op[0] + abcd[1] + op[1] + abcd[2] + op[2] + abcd[3] + "=7"
        break
print(answer)
