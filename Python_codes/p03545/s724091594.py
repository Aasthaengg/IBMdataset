ABCD = input().strip()
for i in range(8):
    ope = [{0:'+', 1:'-'}[(i>>j) & 1] for j in range(3)]
    fomula = ABCD[0] + ope[0] + ABCD[1] + ope[1] + ABCD[2] + ope[2] + ABCD[3]
    if eval(fomula) == 7:
        print(f'{fomula}=7')
        break