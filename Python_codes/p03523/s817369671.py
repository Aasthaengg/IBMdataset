s = list(str(input()))
t = list('AKIHABARA')
s.reverse()
t.reverse()
for i in range(len(t)):
    c = t.pop()
    if s:
        if c == s[-1]:
            s.pop()
        else:
            if c == 'A':
                continue
            else:
                break
    else:
        if c != 'A':
            print('NO')
            exit()
        else:
            continue
if not s:
    print('YES')
else:
    print('NO')
