a,b,c = map(int, input().split())

YN = lambda b: print('YES') if b else print('NO')
YN( b-a==c-b )