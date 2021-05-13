b = input()

if b == 'A':
    answer = 'T'
elif b == 'T':
    answer = 'A'
elif b == 'C':
    answer = 'G'
elif b == 'G':
    answer = 'C'
else:
    answer = '入力間違い【A】【T】【C】【G】を入力'

print(answer)