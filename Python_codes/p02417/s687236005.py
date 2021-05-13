alphabetTable = dict.fromkeys([chr(i) for i in range(97, 123)], 0)

while True:
    try:
        for text in input():
            for i in range(len(text)):
                if text[i].lower() in alphabetTable:
                    alphabetTable[text[i].lower()] += 1
    except EOFError:
        break

for r in sorted(alphabetTable):
    print(r,':',alphabetTable[r])