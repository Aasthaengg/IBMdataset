nyuryoku = []

try:
    while True:
        s = input()
        if s == 0:
            break
        nyuryoku.append(s)

except EOFError:
    pass

for i in range(len(nyuryoku) - 1):
    print('Case ' + str(i + 1) + ": " + str(nyuryoku[i]))
