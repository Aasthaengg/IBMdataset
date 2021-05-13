l, n, r = set(), int(input()), str.maketrans('ACGT', '1234')

for _ in range(n):
    opr, word = input().split()
    word = int(word.translate(r), base=5)
    if opr.startswith('i'):
        l.add(word)
    else:
        print('yes' if word in l else 'no')