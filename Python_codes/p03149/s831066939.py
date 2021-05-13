s = list('1974')
for n in input().split():
    if(not n in s):
        print('NO')
        break
    else:
        s.remove(n)
else:
    print('YES')
