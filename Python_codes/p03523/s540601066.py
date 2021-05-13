S = input()
ch = 0
if S == 'AKIHABARA':
    ch = 1
elif S == 'KIHABARA' or S == 'AKIHBARA' or S == 'AKIHABRA' or S == 'AKIHABAR' or S == 'AKIHABARA' or S == 'AKIHABARA':
    ch = 1
elif S == 'KIHBARA' or S == 'KIHABRA' or S == 'KIHABAR':
    ch = 1
elif S == 'AKIHBRA' or S == 'AKIHBAR':
    ch = 1
elif S == 'AKIHABR':
    ch = 1
elif S == 'KIHBRA' or S == 'KIHBAR' or S == 'KIHABR':
    ch = 1
elif S == 'AKIHBR':
    ch = 1
elif S == 'KIHBR':
    ch = 1

if ch == 0:
    print('NO')
else:
    print('YES')
