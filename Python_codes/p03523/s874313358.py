s = input()
if len(s) > 9:
    print('NO')
elif s == 'AKIHABARA' or \
     s == 'AKIHABAR' or \
     s == 'AKIHABRA' or \
     s == 'AKIHBARA' or \
     s == 'KIHABARA' or \
     s == 'AKIHABR' or \
     s == 'AKIHBAR' or \
     s == 'KIHABAR' or \
     s == 'AKIHBRA' or \
     s == 'KIHABRA' or \
     s == 'KIHBARA' or \
     s == 'AKIHBR' or \
     s == 'KIHBRA' or \
     s == 'KIHABR' or \
     s == 'KIHBAR' or \
     s == 'KIHBR':
    print('YES')
else:
    print('NO')

