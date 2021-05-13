S = input()

if S == 'ooo':
    y = 700 + 300
if S == 'oox' or S == 'oxo' or S == 'xoo':
    y = 700 + 200
if S == 'oxx' or S == 'xox' or S == 'xxo':
    y = 700 + 100
if S == 'xxx':
    y = 700
    
print(str(y))