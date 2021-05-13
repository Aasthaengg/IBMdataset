s = str(input())
t = s.replace('eraser', '').replace('erase', '').replace('dreamer', '').replace('dream', '')
if t == '':
    print('YES')
else:
    print('NO')
