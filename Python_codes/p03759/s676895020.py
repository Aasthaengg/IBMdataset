a, b, c = map(int,input().split())
if (a-b)==(b-c) or (b-a)==(c-b):
    print('YES')
else:
    print('NO')