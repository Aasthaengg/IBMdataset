S = input()

letter = []
for i in range(65, 91):
    letter.append(S.count(chr(i)))
letter = sorted(letter, reverse=True)
if letter[0] == 2 and letter[1] == 2:
    print('Yes')
else:
    print('No')
