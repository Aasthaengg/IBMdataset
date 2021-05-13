S = input()
s = set(S)
count = [S.count(i) for i in s]
if len(S) == 2:
    if len(s) == 2:
        print('YES')
    else:
        print('NO')
elif (max(count)-min(count) <= 1 and len(s) == 3) or len(S) == 1:
    print('YES')
else:
    print('NO')
