inn = input()
numR = 0
for c in inn:
    if c == 'R':
        numR += 1
if numR != 2:
    print(numR)
else:
    print(1 if inn[1] == 'S' else 2)