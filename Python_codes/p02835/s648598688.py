a1, a2, a3 = map(int, input().split())
total = a1+a2+a3
if total <= 21:
    print('win')
else:
    print('bust')